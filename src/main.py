from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType
from split_nodes import *
from markdown_blocks import *
from md_to_html import markdown_to_html_node

def main():
    md = """
This is text with an ![image](haha.com)

This has a [link](lol.com)
and some _shi_

- you know what
- this ain't that bad

1. The tough one is
2. Maybe this **one**
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    print(html)
    print("""<div><p>This is text with an <img src="haha.com" alt="image"></img></p><p>This has a <a href="lol.com">link</a> and some <i>shi</i></p><ul><li>you know what</li><li>this ain't that bad</li></ul><ol><li>The tough one is</li><li>Maybe this <b>one</b></li></ol></div>""")
main()