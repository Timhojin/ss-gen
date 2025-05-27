from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType
from split_nodes import *

def main():
    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) ",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    for new_node in new_nodes:
        print(new_node)
main()