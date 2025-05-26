from textnode import TextNode, TextType

def main():
    tnode = TextNode("this is a text", TextType.TEXT, "www.google.com.au.ua")
    tode = TextNode("this is a text", TextType.TEXT, "www.google.com.au.ua")
    print(tnode == tode)
    print(tnode)

main()