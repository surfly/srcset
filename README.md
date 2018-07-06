srcset
=====

[srcset attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-srcset) parser

## How to use
```python
from srcset.srcset import SRCSet

obj = SRCSet("/q_auto,f_auto/image.png?a 1w, image2.png")
obj.parse()

# [{u'h': None, u'url': '/q_auto,f_auto/image.png?a', u'w': u'1', u'x': None},
# {u'h': None, u'url': 'image2.png', u'w': None, u'x': None}]

obj.candidates[1]["w"] = 2
obj.stringify()

# u'/q_auto,f_auto/image.png?a 1w, image2.png 2w'
```
