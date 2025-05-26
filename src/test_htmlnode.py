import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("h1", "this is a heading", None, {"href": "google.com"})
        ans = """HTMLNode(
tag=h1,
value=this is a heading,
children=None,
props=href="google.com"
)"""
        self.assertEqual(node.__repr__(), ans)

    def test_props(self):
        node = HTMLNode("a", None, None, {"href": "google.ooiiaaoo", "target": "_blank"})
        ans = '''href="google.ooiiaaoo" target="_blank"'''
        self.assertEqual(node.props_to_html(), ans)