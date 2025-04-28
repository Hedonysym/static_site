import unittest

from textnode import TextNode, TextType

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
               

if __name__ == "__main__":
    unittest.main()