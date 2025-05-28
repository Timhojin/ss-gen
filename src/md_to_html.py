from markdown_blocks import *
from htmlnode import *
from textnode import TextNode, TextType
from textnode_htmlnode import text_node_to_html_node
from split_nodes import text_to_textnodes

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    return html_nodes

def ulist_to_htmlnode(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def olist_to_htmlnode(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def quote_htmlnode(block):
    html_nodes = []
    for line in block.split("\n"):
        html_node = None
        clear_line = line.strip(">").strip()
        children = text_to_children(clear_line)
        html_node = ParentNode("li", children)

        html_nodes.append(html_node)
    return ParentNode("ul", html_nodes)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)
        html_node = None
        match (block_type):
            case (BlockType.PARAGRAPH):
                value = " ".join(block.split("\n"))
                children = text_to_children(value)
                html_node = ParentNode("p", children)
            case (BlockType.HEADING):
                n = block[:6].count("#")
                value = " ".join(block.split("\n"))
                value = value.strip("#").strip()
                children = text_to_children(value)
                html_node = ParentNode(f"h{n}", children)
            case (BlockType.QUOTE):
                html_node = quote_htmlnode(block)
            case (BlockType.ULIST):
                html_node = ulist_to_htmlnode(block)
            case (BlockType.OLIST):
                html_node = olist_to_htmlnode(block)
            case (BlockType.CODE):
                if not block.startswith("```") or not block.endswith("```"):
                    raise ValueError("invalid code block")
                text = block[4:-3]
                raw_text_node = TextNode(text, TextType.TEXT)
                child = text_node_to_html_node(raw_text_node)
                code = ParentNode("code", [child])
                html_node = ParentNode("pre", [code])
            case _:
                raise ValueError("invalid block type")
        html_nodes.append(html_node)
    return ParentNode("div", html_nodes)