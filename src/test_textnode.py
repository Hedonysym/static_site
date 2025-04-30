import unittest

from textnode import *
from htmlnode import *
from parser import *


class TestTextNodeimageandurlgrab(unittest.TestCase):
    def test1(self):
        block = "### fuck"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test2(self):
        block = "####### fuck"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test3(self):
        block = "> fuck\n> you\n >bitch"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    
    def test4(self):
        block = "- shit\n- piss\n# fuck"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test5(self):
        block = "```\nfuck = shit.piss\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

        

if __name__ == "__main__":
    unittest.main()