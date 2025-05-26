from textnode import TextNode, TextType

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