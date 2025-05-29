import unittest

from split_nodes import extract_title

class TestTitle(unittest.TestCase):
    def test_one_line(self):
        md = """# This is a title"""
        title = extract_title(md)
        self.assertEqual(title, "This is a title")

    def test_mutiple_lines(self):
        md = """
this is not a title

# Thi sia title"""

        title = extract_title(md)
        self.assertEqual(title, "Thi sia title")

    def test_no_header(self):
        md = """
asads
asd
sa
d
sadd#

### asasa"""
        with self.assertRaises(Exception):
            extract_title(md)