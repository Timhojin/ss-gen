from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType
from split_nodes import *
from markdown_blocks import *
from md_to_html import markdown_to_html_node
from data_stuff import copye, generate_page

def main():
    src = "static"
    dest = "public"
    copye(src, dest)
    generate_page("content/index.md", "template.html", "public/index.html")

main()