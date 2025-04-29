import unittest

from textnode import *
from htmlnode import *
from parser import *


class TestTextNodeimageandurlgrab(unittest.TestCase):
    def test_1(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        print(extract_markdown_images(text))
        self.assertEqual(extract_markdown_images(text), [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
  
    def test_2(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        print(extract_markdown_links(text))
        self.assertEqual(extract_markdown_links(text), [("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
  


if __name__ == "__main__":
    unittest.main()