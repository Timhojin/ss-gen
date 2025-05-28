import unittest

from md_to_html import markdown_to_html_node

class TestMdToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_mixed_content(self):
        md = """
This is text with an

This has a
and some _shi_

- you know what
- this ain't that bad

1. The tough one is
2. Maybe this **one**
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            """<div><p>This is text with an</p><p>This has a and some <i>shi</i></p><ul><li>you know what</li><li>this ain't that bad</li></ul><ol><li>The tough one is</li><li>Maybe this <b>one</b></li></ol></div>""",
        )

    def test_link_and_image(self):
        md = """
this has a [link](bro.com)

and another ![image](broda.png)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            """<div><p>this has a <a href="bro.com">link</a></p><p>and another <img src="broda.png" alt="image"></img></p></div>"""
        )