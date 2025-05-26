import unittest

from textnode_htmlnode import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import LeafNode

class TestTextnToHTMLn(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("blank image", TextType.IMAGE, "not_image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props_to_html(), '''src="not_image.png" alt="blank image"''')
    
    def test_code(self):
        node = TextNode("import zlib", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "import zlib")

    def test_link(self):
        node = TextNode("tap to enter the void", TextType.LINK, "instagram.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "instagram.com"})