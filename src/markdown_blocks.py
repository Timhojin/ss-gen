from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_llist"

def block_to_block_type(block):
    if not block:
        return BlockType.PARAGRAPH
        
    def check_olist():
        lines = block.split('\n')
        expected_number = 1
        for line in lines:
            index = line.index(".")
            if str(expected_number) != line[:index]:
                return False
            expected_number += 1
        return True

    if block[0] == "#":
        return BlockType.HEADING
    elif block[:3] == "```" and block[-3:] == "```":
        return BlockType.CODE
    elif len(block.split("\n")) == sum(1 for line in block.split("\n") if line[0] == ">"):
        return BlockType.QUOTE
    elif len(block.split("\n")) == sum(1 for line in block.split("\n") if line[0] == "-"):
        return BlockType.ULIST
    elif block[1] == "." and check_olist():
        return BlockType.OLIST
    else:
        return BlockType.PARAGRAPH
        
def markdown_to_blocks(md):
    blocks = md.split("\n\n")
    new_blocks = []
    for block in blocks:
        if len(block) == 0:
            continue

        block = block.strip()
        new_blocks.append(block)

    # for block in new_blocks:
    #     print(block + "-")
    return new_blocks