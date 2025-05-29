from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType
from split_nodes import *
from markdown_blocks import *
from md_to_html import markdown_to_html_node
from copy_data import copye

def main():
    src = "static"
    dest = "public"
    copye(src, dest)

main()