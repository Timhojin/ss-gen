from textnode import TextNode, TextType
import re

def extract_title(markdown):
    for line in markdown.split("\n\n"):
        if line.strip()[:2] == "# ":
            return " ".join(line.strip("#").strip().split("\n"))
    raise Exception("H1 not found")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        if old_node.text.count(delimiter) % 2 == 1:
            raise Exception("closing delimiter missing")
        
        splitted = old_node.text.split(delimiter)
        is_text = False
        for i in range(len(splitted)):
            is_text = not is_text
            if len(splitted[i]) == 0:
                continue
            elif is_text:
                new_nodes.append(TextNode(splitted[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(splitted[i], text_type))

    return new_nodes

def extract_markdown_images(text):
    image_captures = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return image_captures

def extract_markdown_links(text):
    link_captures = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return link_captures

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        matches = extract_markdown_images(old_node.text)
        text = old_node.text
        for alt, link in matches:
            match_bracketed = (f"![{alt}]({link})")
            first, text = text.split(match_bracketed, 1)
            new_nodes.append(TextNode(first, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, link))
        if len(text):
            new_nodes.append(TextNode(text, TextType.TEXT))
        
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        matches = extract_markdown_links(old_node.text)
        text = old_node.text
        for alt, link in matches:
            match_bracketed = (f"[{alt}]({link})")
            first, text = text.split(match_bracketed, 1)
            new_nodes.append(TextNode(first, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.LINK, link))
        if len(text):
            new_nodes.append(TextNode(text, TextType.TEXT))
        
    return new_nodes

def text_to_textnodes(text):
    nodes = split_nodes_link([TextNode(text, TextType.TEXT)])
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

    return nodes
    