from htmlnode import *
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        if delimiter not in node.text:
            raise Exception("invalid markdown syntax")
        split = node.text.split(delimiter)
        new_nodes.extend(
            map(lambda n, t: TextNode(n.replace(delimiter, ""), t) , 
                filter(None, split), 
                [TextType.TEXT, text_type, TextType.TEXT]))
    return new_nodes
