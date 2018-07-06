"""
Reference https://chromium.googlesource.com/chromium/src/+/66.0.3359.158/third_party/WebKit/LayoutTests/external/wpt/html/semantics/embedded-content/the-img-element/srcset/parse-a-srcset-attribute.html
"""

import argparse
import unittest
import timeit

from srcset import SRCSet

LOOP_SIZE = 10000
REPEAT = 3


class TestLoop(unittest.TestCase):
    def test_1(self):
        string = ""
        expected = []
        result = ""
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_2(self):
        string = ","
        expected = []
        result = ""
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_3(self):
        string = ",,,"
        expected = []
        result = ""
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_4(self):
        string = "  data:,a  1x  "
        expected = [{
            "url": "data:,a",
            "x": "1",
            "w": None,
            "h": None
        }]
        result = "data:,a 1x"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_5(self):
        string = "\t\tdata:,a\t\t1x\t\t"
        expected = [{
            "url": "data:,a",
            "x": "1",
            "w": None,
            "h": None
        }]
        result = "data:,a 1x"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_6(self):
        string = "\u000Adata:,a\u000A1x\u000A".decode("unicode-escape")
        expected = [{
            "url": "data:,a",
            "x": "1",
            "w": None,
            "h": None
        }]
        result = "data:,a 1x"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_7(self):
        string = "\u000B\u000Bdata:,a\u000B\u000B1x\u000B\u000B".decode("unicode-escape")
        expected = [{
            "url": "\x0b\x0bdata:,a\x0b\x0b1x\x0b\x0b",
            "x": None,
            "w": None,
            "h": None
        }]
        result = "\x0b\x0bdata:,a\x0b\x0b1x\x0b\x0b"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_8(self):
        string = "\u000Cdata:,a\u000C1x\u000C".decode("unicode-escape")
        expected = [{
            "url": "data:,a",
            "x": "1",
            "w": None,
            "h": None
        }]
        result = "data:,a 1x"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_9(self):
        string = "\u000Ddata:,a\u000D1x\u000D".decode("unicode-escape")
        expected = [{
            "url": "data:,a",
            "x": "1",
            "w": None,
            "h": None
        }]
        result = "data:,a 1x"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_10(self):
        string = "\u000Edata:,a\u000E1x\u000E".decode("unicode-escape")
        expected = [{
            "url": "\x0edata:,a\x0e1x\x0e",
            "x": None,
            "w": None,
            "h": None
        }]
        result = "\x0edata:,a\x0e1x\x0e"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_11(self):
        string = "data:,a"
        expected = [{
            "url": "data:,a",
            "x": None,
            "w": None,
            "h": None
        }]
        result = "data:,a"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_12(self):
        string = "data:,a "
        expected = [{
            "url": "data:,a",
            "x": None,
            "w": None,
            "h": None
        }]
        result = "data:,a"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_13(self):
        string = "data:,a ,"
        expected = [{
            "url": "data:,a",
            "x": None,
            "w": None,
            "h": None
        }]
        result = "data:,a"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_14(self):
        string = "data:,a,"
        expected = [{
            "url": "data:,a",
            "x": None,
            "w": None,
            "h": None
        }]
        result = "data:,a"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_15(self):
        string = "data:,a, "
        expected = [{
            "url": "data:,a",
            "x": None,
            "w": None,
            "h": None
        }]
        result = "data:,a"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_16(self):
        string = "data:,a,,,"
        expected = [{
            "url": "data:,a",
            "x": None,
            "w": None,
            "h": None
        }]
        result = "data:,a"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_17(self):
        string = "data:,a,, , "
        expected = [{
            "url": "data:,a",
            "x": None,
            "w": None,
            "h": None
        }]
        result = "data:,a"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_18(self):
        string = " data:,a"
        expected = [{
            "url": "data:,a",
            "x": None,
            "w": None,
            "h": None
        }]
        result = "data:,a"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_19(self):
        string = ",,,data:,a"
        expected = [{
            "url": "data:,a",
            "x": None,
            "w": None,
            "h": None
        }]
        result = "data:,a"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_20(self):
        string = " , ,,data:,a"
        expected = [{
            "url": "data:,a",
            "x": None,
            "w": None,
            "h": None
        }]
        result = "data:,a"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_21(self):
        string = "&nbsp;data:,a"
        expected = [{
            "url": "&nbsp;data:,a",
            "x": None,
            "w": None,
            "h": None
        }]
        result = "&nbsp;data:,a"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_22(self):
        string = "data:,a&nbsp;"
        expected = [{
            "url": "data:,a&nbsp;",
            "x": None,
            "w": None,
            "h": None
        }]
        result = "data:,a&nbsp;"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)


class TestTokenizer(unittest.TestCase):
    def test_1(self):
        string = "data:,a 1x"
        expected = [{
            "url": "data:,a",
            "x": "1",
            "w": None,
            "h": None
        }]
        result = "data:,a 1x"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_2(self):
        string = "data:,a 1x "
        expected = [{
            "url": "data:,a",
            "x": "1",
            "w": None,
            "h": None
        }]
        result = "data:,a 1x"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_3(self):
        string = "data:,a 1x,"
        expected = [{
            "url": "data:,a",
            "x": "1",
            "w": None,
            "h": None
        }]
        result = "data:,a 1x"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_4(self):
        string = "data:,a ( , data:,b 1x, ), data:,c"
        expected = [{
            "url": "data:,c",
            "x": None,
            "w": None,
            "h": None
        },
        ]
        result = "data:,c"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_5(self):
        string = "data:,a ((( , data:,b 1x, ), data:,c"
        expected = [{
            "url": "data:,c",
            "x": None,
            "w": None,
            "h": None
        }]
        result = "data:,c"
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)

    def test_6(self):
        string = "data:,a [ , data:,b 1x, ], data:,c"
        expected = [
            {
                "url": "data:,b",
                "x": "1",
                "w": None,
                "h": None
            },
            {
                "url": "]",
                "x": None,
                "w": None,
                "h": None
            },
            {
                "url": "data:,c",
                "x": None,
                "w": None,
                "h": None
            }
        ]
        result = "data:,b 1x, ], data:,c"
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_7(self):
        string = "data:,a { , data:,b 1x, }, data:,c"
        expected = [
            {
                "url": "data:,b",
                "x": "1",
                "w": None,
                "h": None
            },
            {
                "url": "}",
                "x": None,
                "w": None,
                "h": None
            },
            {
                "url": "data:,c",
                "x": None,
                "w": None,
                "h": None
            }
        ]
        result = "data:,b 1x, }, data:,c"
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_8(self):
        string = 'data:,a " , data:,b 1x, ", data:,c'
        expected = [
            {
                "url": "data:,b",
                "x": "1",
                "w": None,
                "h": None
            },
            {
                "url": '"',
                "x": None,
                "w": None,
                "h": None
            },
            {
                "url": "data:,c",
                "x": None,
                "w": None,
                "h": None
            }
        ]
        result = "data:,b 1x, \", data:,c"
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_9(self):
        string = "data:,a ,data:;,b, data:,c"
        expected = [
            {
                "url": "data:,a",
                "x": None,
                "w": None,
                "h": None
            },
            {
                "url": 'data:;,b',
                "x": None,
                "w": None,
                "h": None
            },
            {
                "url": "data:,c",
                "x": None,
                "w": None,
                "h": None
            }
        ]
        result = "data:,a, data:;,b, data:,c"
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_10(self):
        string = "data:,a, data:,b ("
        expected = [
            {
                "url": "data:,a",
                "x": None,
                "w": None,
                "h": None
            }
        ]
        result = "data:,a"
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_11(self):
        string = "data:,a, data:,b (  "
        expected = [
            {
                "url": "data:,a",
                "x": None,
                "w": None,
                "h": None
            }
        ]
        result = "data:,a"
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_12(self):
        string = "data:,a, data:,b (,"
        expected = [
            {
                "url": "data:,a",
                "x": None,
                "w": None,
                "h": None
            }
        ]
        result = "data:,a"
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_13(self):
        string = "data:,a, data:,b (x"
        expected = [
            {
                "url": "data:,a",
                "x": None,
                "w": None,
                "h": None
            }
        ]
        result = "data:,a"
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_14(self):
        string = "data:,a, data:,b ()"
        expected = [
            {
                "url": "data:,a",
                "x": None,
                "w": None,
                "h": None
            }
        ]
        result = "data:,a"
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_15(self):
        string = "data:,a (, data:,b"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_16(self):
        string = "data:,a /*, data:,b, data:,c */"
        expected = [
            {
                "url": "data:,b",
                "x": None,
                "w": None,
                "h": None
            }
        ]
        result = "data:,b"
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_17(self):
        string = "data:,a //, data:,b"
        expected = [
            {
                "url": "data:,b",
                "x": None,
                "w": None,
                "h": None
            }
        ]
        result = "data:,b"
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)


class TestDescriptor(unittest.TestCase):
    def test_1(self):
        string = "data:,a foo"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_2(self):
        string = "data:,a foo foo"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_3(self):
        string = "data:,a foo 1x"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_4(self):
        string = "data:,a foo 1x foo"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_5(self):
        string = "data:,a foo 1w"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_6(self):
        string = "data:,a foo 1w foo"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_7(self):
        string = "data:,a 1x 1x"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_8(self):
        string = "data:,a 1w 1w"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_9(self):
        string = "data:,a 1w 1x"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_10(self):
        string = "data:,a 1x 1w"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_11(self):
        string = "data:,a 1w 1h"
        expected = [
            {
                "url": "data:,a",
                "x": None,
                "w": "1",
                "h": "1"
            }
        ]
        result = "data:,a 1w 1h"
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_12(self):
        string = "data:,a 1h 1w"
        expected = [
            {
                "url": "data:,a",
                "x": None,
                "w": "1",
                "h": "1"
            }
        ]
        result = "data:,a 1w 1h"
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_13(self):
        string = "data:,a 1h 1h"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_14(self):
        string = "data:,a 1h 1x"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_15(self):
        string = "data:,a 1h 1w 1x"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_16(self):
        string = "data:,a 1x 1w 1h"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_17(self):
        string = "data:,a 1w"
        expected = [
            {
                "url": "data:,a",
                "x": None,
                "w": "1",
                "h": None
            }
        ]
        result = "data:,a 1w"
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_18(self):
        string = "data:,a 1h"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_19(self):
        string = "data:,a 1h foo"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_20(self):
        string = "data:,a foo 1h"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_21(self):
        string = "data:,a 0w"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_22(self):
        string = "data:,a -1w"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_23(self):
        string = "data:,a 1w -1w"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_24(self):
        string = "data:,a 1.0w"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_25(self):
        string = "data:,a 1w 1.0w"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_26(self):
        string = "data:,a 1e0w"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_27(self):
        string = "data:,a 1w 1e0w"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_28(self):
        string = "data:,a 1www"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_29(self):
        string = "data:,a 1w 1www"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_30(self):
        string = "data:,a +1w"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_31(self):
        string = "data:,a 1w +1w"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_32(self):
        string = "data:,a 1W"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_33(self):
        string = "data:,a 1w 1W"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_34(self):
        string = "data:,a Infinityw"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_35(self):
        string = "data:,a 1w Infinityw"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_36(self):
        string = "data:,a NaNw"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_37(self):
        string = "data:,a 1w NaNw"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_38(self):
        string = "data:,a 0x1w"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_39(self):
        string = "data:,a 0X1w"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_40(self):
        string = "data:,a 0X1w"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_41(self):
        string = "data:,a 1&#x1;w"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_42(self):
        string = "data:,a 1&nbsp;w"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_43(self):
        string = "data:,a 1&#x1680;w"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_44(self):
        string = "data:,a 1&#x2000;w"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_45(self):
        string = "data:,a 1&#x2001;w"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_46(self):
        string = "data:,a 0x"
        expected = [
            {
                "url": "data:,a",
                "x": "0",
                "w": None,
                "h": None
            }
        ]
        result = "data:,a 0x"
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_47(self):
        string = "data:,a -0x"
        expected = [
            {
                "url": "data:,a",
                "x": "-0",
                "w": None,
                "h": None
            }
        ]
        result = "data:,a -0x"
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_48(self):
        string = "data:,a 1x -0x"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_49(self):
        string = "'data:,a -1x"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_50(self):
        string = "data:,a 1x -1x"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_51(self):
        string = "data:,a 1e0x"
        expected = [
            {
                "url": "data:,a",
                "x": "1e0",
                "w": None,
                "h": None
            }
        ]
        result = "data:,a 1e0x"
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_52(self):
        string = "data:,a 1E0x"
        expected = [
            {
                "url": "data:,a",
                "x": "1E0",
                "w": None,
                "h": None
            }
        ]
        result = "data:,a 1E0x"
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_53(self):
        string = "data:,a 1e-1x"
        expected = [
            {
                "url": "data:,a",
                "x": "1e-1",
                "w": None,
                "h": None
            }
        ]
        result = "data:,a 1e-1x"
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_54(self):
        string = "data:,a 1.5e1x"
        expected = [
            {
                "url": "data:,a",
                "x": "1.5e1",
                "w": None,
                "h": None
            }
        ]
        result = "data:,a 1.5e1x"
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_55(self):
        string = "data:,a -x"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_56(self):
        string = "data:,a .x"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_57(self):
        string = "data:,a -.x"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_58(self):
        string = "data:,a 1.x"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_59(self):
        string = "data:,a .5x"
        expected = [
            {
                "url": "data:,a",
                "x": ".5",
                "w": None,
                "h": None
            }
        ]
        result = "data:,a .5x"
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_60(self):
        string = "data:,a .5e1x"
        expected = [
            {
                "url": "data:,a",
                "x": ".5e1",
                "w": None,
                "h": None
            }
        ]
        result = "data:,a .5e1x"
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_61(self):
        string = "data:,a 1x 1.5e1x"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_62(self):
        string = "data:,a 1x 1e1.5x"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_63(self):
        string = "data:,a 1.0x"
        expected = [
            {
                "url": "data:,a",
                "x": "1.0",
                "w": None,
                "h": None
            }
        ]
        result = "data:,a 1.0x"
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_64(self):
        string = "data:,a 1x 1.0x"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_65(self):
        string = "data:,a +1x"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_66(self):
        string = "data:,a 1X"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_67(self):
        string = "data:,a Infinityx"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_68(self):
        string = "data:,a NaNx"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_69(self):
        string = "data:,a 0x1x"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_70(self):
        string = "data:,a 0X1x"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_71(self):
        string = "data:,a 1&#x1;x"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_72(self):
        string = "data:,a 1w 0h"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_73(self):
        string = "data:,a 1w -1h"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_74(self):
        string = "data:,a 1w 1.0h"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_75(self):
        string = "data:,a 1w 1e0h"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_76(self):
        string = "data:,a 1w 1hhh"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_77(self):
        string = "data:,a 1w +1h"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_78(self):
        string = "data:,a 1w 1H"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_79(self):
        string = "data:,a 1w Infinityh"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_80(self):
        string = "data:,a 1w NaNh"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_81(self):
        string = "data:,a 0x1h"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_82(self):
        string = "data:,a 0X1h"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)

    def test_83(self):
        string = "data:,a 1w 1&#x1;h"
        expected = []
        result = ""
        obj = SRCSet(string)
        obj.parse()
        self.assertEqual(obj.candidates, expected)
        self.assertEqual(obj.stringify(), result)


class TestSpecific(unittest.TestCase):
    def test_channel(self):
        string = "//www.chanel.com/images/q_auto,f_auto,fl_lossy,dpr_auto/w_128/FSH-18aegamenucollection.jpg"
        expected = [{
            "url": string,
            "w": None,
            "h": None,
            "x": None
        }]
        result = string
        obj = SRCSet(string)
        self.assertEqual(obj.parse(), expected)
        self.assertEqual(obj.stringify(), result)


def benchmark():
    SRCSet("  data:,a  1x  , data:c qw").parse()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-b", "--benchmark",
        default=False,
        action="store_true",
        help="Run benchmark"
    )
    args = parser.parse_args()
    if args.benchmark:
        print(
            "%.3fs (best of %s repeats for %s repetitions)" %
            (
                min(timeit.Timer(
                    'benchmark()', setup="from __main__ import benchmark"
                ).repeat(number=10000)),
                REPEAT,
                LOOP_SIZE,
            )
        )
    else:
        unittest.main()
