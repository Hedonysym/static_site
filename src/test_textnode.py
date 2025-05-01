import unittest

from textnode import *
from htmlnode import *
from inline_markdown import *
from markdown_blocks import *


class TestTextNodeimageandurlgrab(unittest.TestCase):
    def test1(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )
    
    def test2(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )
        
    def test3(self):
        md = """
1. fuck
2. you


why am i even **alive**
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, 
            "<div><ol><li>fuck</li><li>you</li></ol><p>why am i even <b>alive</b></p></div>"
        )
    

if __name__ == "__main__":
    unittest.main()