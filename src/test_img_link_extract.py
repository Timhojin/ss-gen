import unittest

from split_nodes import extract_markdown_images, extract_markdown_links

class TestImageLinkExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This has a [link](google.com)"
        )
        self.assertListEqual([("link", "google.com")], matches)
    
    def test_extract_markdown_multiple_images(self):
        matches = extract_markdown_images(
            "This has ![multiple](google.com.png)! ![images](hahahahha.www.com)."
        )
        self.assertListEqual([("multiple", "google.com.png"), ("images", "hahahahha.www.com")], matches)
    
    def test_extract_markdown_multiple_links(self):
        matches = extract_markdown_links(
            "This has [multiple](google.com.png)! [links](hahahahha.www.com)."
        )
        self.assertListEqual([("multiple", "google.com.png"), ("links", "hahahahha.www.com")], matches)