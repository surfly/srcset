from __future__ import unicode_literals

import math

# See https://infra.spec.whatwg.org/#ascii-whitespace
WHITESPACES = (
    "\u0009",  # \t
    "\u000A",
    "\u000C",
    "\u000D",
    "\u0020"  # " "
)

STATE_IN_DESCRIPTOR = 1
STATE_AFTER_DESCRIPTOR = 2
STATE_IN_PARENS = 3


class SRCSet(object):
    raw = None
    candidates = None

    def __init__(self, string):
        self.raw = string

    def parse(self):
        """
        Based on algorithm from https://html.spec.whatwg.org/multipage/images.html#parse-a-srcset-attribute
        """
        # Step 1, 2, 3
        pos = 0
        candidates = []
        state = None

        # Step 4
        while True:
            pos, _ = collect_characters_in(self.raw, pos, WHITESPACES + (",", ))

            # Step 5
            if pos >= len(self.raw):
                self.candidates = candidates
                return candidates

            # Step 6
            pos, url = collect_characters_out(self.raw, pos, WHITESPACES)

            # Step 7
            descriptors = []

            # Step 8.1
            if url[-1] == ",":
                while len(url) and url[-1] == ",":
                    url = url[:-1]
                # JUMP to descriptor parser
            else:
                # Step 8.e.1
                pos, _ = collect_characters_in(self.raw, pos, WHITESPACES)

                # Step 8.e.2
                current_descriptor = ""
                state = STATE_IN_DESCRIPTOR

                # Step 8.e.4
                while True:
                    if pos < len(self.raw):
                        cc = self.raw[pos]
                    else:
                        cc = None
                    if state == STATE_IN_DESCRIPTOR:
                        if cc in WHITESPACES:
                            if current_descriptor:
                                descriptors.append(current_descriptor)
                                current_descriptor = ""
                                state = STATE_AFTER_DESCRIPTOR
                        elif cc == ",":
                            pos = pos + 1
                            if current_descriptor:
                                descriptors.append(current_descriptor)
                                # JUMP to descriptor parser
                            break
                        elif cc == "(":
                            current_descriptor = current_descriptor + cc
                            state = STATE_IN_PARENS
                        elif cc is None:
                            if current_descriptor:
                                descriptors.append(current_descriptor)
                            # JUMP to descriptor parser
                            break
                        else:
                            current_descriptor = current_descriptor + cc
                    elif state == STATE_IN_PARENS:
                        if cc == ")":
                            current_descriptor = current_descriptor + cc
                            state = STATE_IN_DESCRIPTOR
                        elif cc is None:
                            descriptors.append(current_descriptor)
                            # JUMP to descriptor parser
                            break
                        else:
                            current_descriptor = current_descriptor + cc
                    elif state == STATE_AFTER_DESCRIPTOR:
                        if cc in WHITESPACES:
                            pass
                        elif cc is None:
                            # JUMP to descriptor parser
                            break
                        else:
                            state = STATE_IN_DESCRIPTOR
                            pos = pos - 1
                    pos = pos + 1

            # Step 9, 10, 11, 12 (descriptor parser)
            error = False
            width = None
            density = None
            h = None

            # Step 13
            # print("Descriptors", descriptors)
            for descriptor in descriptors:
                if len(descriptor) >= 2:
                    last_char = descriptor[-1]
                    value = descriptor[:-1]
                    if last_char == "w":
                        try:
                            conv_value = int(value)
                        except ValueError:
                            error = True
                        else:
                            if width or density:
                                error = True
                            elif conv_value <= 0:
                                error = True
                            elif not value.isdigit():
                                error = True
                            else:
                                width = value
                    elif last_char == "x":
                        try:
                            conv_value = float(value)
                        except ValueError:
                            error = True
                        else:
                            if width or density or h:
                                error = True
                            elif conv_value < 0:
                                error = True
                            elif value[-1] == ".":
                                error = True
                            elif value[0] == "+":
                                error = True
                            elif math.isinf(conv_value):
                                error = True
                            elif math.isnan(conv_value):
                                error = True
                            else:
                                density = value
                    elif last_char == "h":
                        try:
                            conv_value = int(value)
                        except ValueError:
                            error = True
                        else:
                            if h or density:
                                error = True
                            elif conv_value <= 0:
                                error = True
                            elif not value.isdigit():
                                error = True
                            else:
                                h = value
                    else:
                        error = True
                else:
                    error = True

            if h and not width:
                error = True

            if not error:
                candidates.append({
                    "url": url,
                    "w": width,
                    "x": density,
                    "h": h
                })
        self.candidates = candidates
        return candidates

    def stringify(self):
        """
        Returns string which is a valid srcset attribute
        """
        result = ""
        for item in self.candidates:
            if result:
                result = result + ", "
            result = result + item["url"]
            if item["w"]:
                result = result + " %sw" % item["w"]
            if item["x"]:
                result = result + " %sx" % item["x"]
            if item["h"]:
                result = result + " %sh" % item["h"]
        return result


def collect_characters_in(string, start, charset):
    """
    Collect all characters from `start` which are part of the `charset`
    """
    pos = start
    while pos < len(string) and string[pos] in charset:
        pos = pos + 1
    return pos, string[start:pos]


def collect_characters_out(string, start, charset):
    """
    Collect all characters from `start` until one of the characters from `charset`
    is found
    """
    pos = start
    while pos < len(string) and string[pos] not in charset:
        pos = pos + 1
    return pos, string[start:pos]
