import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("this is a poop", TextType.TEXT)
        ans = "TextNode(this is a poop, text)"
        self.assertEqual(node.__repr__(), ans)

    def test_ineq(self):
        node = TextNode("this has a link", TextType.LINK, "www.geiyyyy.com.yare/yare")
        not_ans = "TextNode(this has a link, link)"
        self.assertNotEqual(node.__repr__(), not_ans)

if __name__ == "__main__":
    unittest.main()