from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType
from split_nodes import *

def main():
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    nodes = text_to_textnodes(text)
    for n in nodes:
        print(n)
main()