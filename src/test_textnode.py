import unittest

from textnode import *
from htmlnode import *
from parser import split_nodes_delimiter


class TestTextNodeDelimiter(unittest.TestCase):
    def test_1(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        print(new_nodes)
        self.assertEqual(new_nodes, [
    TextNode("This is text with a ", TextType.TEXT, None),
    TextNode("code block", TextType.CODE, None),
    TextNode(" word", TextType.TEXT, None),
    ])

    def test2(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
        print(new_nodes)
        self.assertEqual(new_nodes, [
    TextNode("This is text with a ", TextType.TEXT, None),
    TextNode("bold", TextType.BOLD, None),
    TextNode(" word", TextType.TEXT, None),])


if __name__ == "__main__":
    unittest.main()