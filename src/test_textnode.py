import unittest

from textnode import *
from htmlnode import *
from inline_markdown import *
from markdown_blocks import *


class TestTextNodeimageandurlgrab(unittest.TestCase):
    def test1(self):
        md = """
# head
## wrong head
# nigga bicth
"""
        self.assertEqual(extract_title(md), "head")
    

if __name__ == "__main__":
    unittest.main()