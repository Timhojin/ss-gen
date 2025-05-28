import unittest

from markdown_blocks import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):
    def test_paragraph(self):
        block = "This is a just a normal paragraph bro"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading(self):
        block = "# This is  aheading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_code(self):
        block = """```this is a code
        block bro```"""
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote(self):
        block = """>This is a quote bro
>and another line of quote man
>lolze lolze"""
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_ulist(self):
        block = """-now this is
- a frikin ulist
- an unorderelsists"""
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)

    def test_olist(self):
        block = """1. Now the tricky one
2. The most feared
3. The most dangerous
4. The toughest
5. Has a white hair
6. The-------
7. TTHEEE
8. a few more to go
9. THEEEEEEEEEE
10. ORDERED LIST"""
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)