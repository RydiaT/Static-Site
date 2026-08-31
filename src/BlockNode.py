from enum import Enum
from TextParse import text_to_textnodes
from textnode import text_node_to_html_node, TextType, TextNode, LeafNode
from htmlnode import HTMLNode, ParentNode

class BlockType(Enum):
    PARAGRAPH = 0
    HEADING = 1
    CODE = 2
    QUOTE = 3
    UNORDERED_LIST = 4
    ORDERED_LIST = 5


def markdown_to_blocks(markdown: str) -> list[str]:
    chunks = markdown.split("\n\n")

    blocks = []
    for chunk in chunks:
        if not chunk.strip():
            continue

        chunk.strip()
        blocks.append(chunk)

    return blocks

def block_to_block_type(block: str) -> BlockType:
    flat_block = block.strip("\n")

    # Heading Check
    first_7 = flat_block[:7]

    if 1 <= first_7.count("#") < 7:
        return BlockType.HEADING

    # Code
    if flat_block[:4] == "```\n" and flat_block[-3:] == "```":
        return BlockType.CODE

    # Quote
    lines = block.split("\n")
    is_quote = True
    for line in lines:
        if line[0] != ">":
            is_quote = False
            break

    if is_quote:
        return BlockType. QUOTE

    # Un-List
    lines = block.split("\n")
    is_list = True
    for line in lines:
        if line[0] != "-" or line[1] != " ":
            is_list = False
            break

    if is_list:
        return BlockType.UNORDERED_LIST

    # List
    lines = block.split("\n")
    is_list = True
    index = 0
    for line in lines:
        if line[0].isnumeric():
            if not (int(line[0]) > index and line[1] == "." and line[2] == " "):
                is_list = False;
                break;
            else:
                index += 1
        else:
            is_list = False;
            break;

    if is_list:
        return BlockType.ORDERED_LIST

    # Paragraph
    return BlockType.PARAGRAPH

def parse_paragraph(block):
    nodes = text_to_textnodes(block.replace("\n", " "))

    children = []

    for node in nodes:
        children.append(text_node_to_html_node(node))

    return ParentNode("p", children)

def parse_code(block):
    node = text_node_to_html_node(TextNode(block[4:-4], TextType.CODE))

    return ParentNode("pre", [node])

def parse_quote(block):
    lines = block.split("> ")

    children = []

    for line in lines:
        if line.split():
            nodes = text_to_textnodes(line)

            for node in nodes:
                children.append(text_node_to_html_node(node))

    return ParentNode("blockquote", children)

def parse_ulist(block):
    lines = block.split("- ")

    children = []

    for line in lines:
        if line.split():
            text_nodes = text_to_textnodes(line)
            nodes = []

            for node in text_nodes:
                nodes.append(text_node_to_html_node(node))

            children.append(ParentNode("li", nodes))

    return ParentNode("ul", children)

def parse_olist(block):
    lines = block.split("\n")

    children = []

    for line in lines:
        if line.split():
            line = line[3:]

            text_nodes = text_to_textnodes(line)
            nodes = []

            for node in text_nodes:
                nodes.append(text_node_to_html_node(node))

            children.append(ParentNode("li", nodes))

    return ParentNode("ol", children)

def parse_heading(block):
    nodes = text_to_textnodes(block[block[:-6].count("#") + 1:])
    children = []

    for node in nodes:
        children.append(text_node_to_html_node(node))

    return ParentNode("h" + str(block[:-6].count("#")), children)



def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    out = []

    for block in blocks:
        type = block_to_block_type(block)

        if type == BlockType.PARAGRAPH:
            out.append(parse_paragraph(block))
        if type == BlockType.CODE:
            out.append(parse_code(block))
        if type == BlockType.QUOTE:
            out.append(parse_quote(block))
        if type == BlockType.UNORDERED_LIST:
            out.append(parse_ulist(block))
        if type == BlockType.ORDERED_LIST:
            out.append(parse_olist(block))
        if type == BlockType.HEADING:
            out.append(parse_heading(block))

    return ParentNode("div", out)

md = """```
This is text that _should_ remain
the **same** even with inline stuff```
"""

print(markdown_to_html_node(md).to_html())