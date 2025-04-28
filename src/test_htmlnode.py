import unittest

from htmlnode import HTMLNode

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
               

if __name__ == "__main__":
    unittest.main()