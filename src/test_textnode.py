import unittest

from textnode import *
from htmlnode import *


class TestParentNode(unittest.TestCase):
    def test_1(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_2(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
           parent_node.to_html(),
           "<div><span><b>grandchild</b></span></div>")

    def test_3(self):
        node1 = LeafNode("b", "bold")
        node2 = LeafNode("i", "image", {"url": "bs.com"})
        node3 = LeafNode(None, "normal")
        parent = ParentNode("p", [node1, node2, node3])
        self.assertEqual(
            parent.to_html(),
            '<p><b>bold</b><i url="bs.com">image</i>normal</p>'
        )

    def test_4(self):
        node = ParentNode("p", None)
        self.assertRaises(ValueError)

if __name__ == "__main__":
    unittest.main()