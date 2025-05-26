import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_without_children(self):
        node = ParentNode("p", [], None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_without_tag(self):
        node = ParentNode("", [LeafNode("span", "child")])
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_to_html_with_tricky_children(self):
        grandchild_node = LeafNode("p", "I'm a grandchild")
        grandchild_node_link = LeafNode("a", "link", {"href": "google.om"})
        child_node = ParentNode("div", [grandchild_node, grandchild_node_link])
        parent = ParentNode("div", [child_node], {"texteditable": "true"})

        self.assertEqual(
            parent.to_html(),
            '''<div texteditable="true"><div><p>I'm a grandchild</p><a href="google.om">link</a></div></div>'''
        )