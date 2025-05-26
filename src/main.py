from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType

def main():
    node = TextNode("This is text with a `code block``another code` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)


main()