import unittest

from htmlnode import HTMLNode, LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "LIINK", {"href": "google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '''<a href="google.com" target="_blank">LIINK</a>''')