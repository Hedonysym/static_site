import unittest

from textnode import *
from htmlnode import *

"""
class TestHTMLNode(unittest.TestCase):
    def test_1(self):
        node = HTMLNode("hi")
        node2 = HTMLNode("hi")
        print(node.__repr__())
        print(node2.__repr__())
        self.assertEqual(node.__repr__(), node2.__repr__())
    
    def test_2(self):
        node = HTMLNode("guacamole", "nigga", None, {"pe": "nis"})
        node2 = HTMLNode("fuck", "shit", None, {"ass": "bitch"})
        print(node.__repr__())
        print(node2.__repr__())
        self.assertNotEqual(node, node2)

    def test_3(self):
        node = HTMLNode("a", "b", ["c"], {"d": "e", "f": "g"})
        expected = " d=\"e\" f=\"g\""
        print(node.__repr__())
        print(node.props_to_html())
        self.assertEqual(node.props_to_html(), expected)
"""
"""
class TestTextNode(unittest.TestCase):
    def test_1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_2(self):
        node = TextNode("This is a text node", TextType.IMAGE, "guacamole.nigga.penis")
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertNotEqual(node, node2)

    def test_3(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node", TextType.NORMAL, "cock.coma")
        self.assertNotEqual(node, node2)
"""
class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), f'<a href="https://www.google.com">Click me!</a>')

    def test3(self):
        node = LeafNode(None, "Guacamole nigga penis. :)")
        print(node.to_html())
        self.assertTrue(node.to_html(), "Guacamole nigga penis. :)")

    def test4(self):
        node = LeafNode("i", None)
        self.assertRaises(ValueError)
               

if __name__ == "__main__":
    unittest.main()