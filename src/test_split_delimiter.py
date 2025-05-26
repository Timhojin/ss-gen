import unittest

from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        answer = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertListEqual(new_nodes, answer)
    
    def test_bold(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        answer = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT),
        ]
        self.assertListEqual(new_nodes, answer)

    def test_adjacent(self):
        node = TextNode("This is text with a `code block``another code` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        answer = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode("another code", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertListEqual(new_nodes, answer)

    def test_first(self):
        node = TextNode("`Code` This is text with a `code block``another code` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        answer = [
            TextNode("Code", TextType.CODE),
            TextNode(" This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode("another code", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertListEqual(new_nodes, answer)
        
    def test_last(self):
        node = TextNode("`Code` This is text with a `code block``another code` `word`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        answer = [
            TextNode("Code", TextType.CODE),
            TextNode(" This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode("another code", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("word", TextType.CODE),
        ]
        self.assertListEqual(new_nodes, answer)