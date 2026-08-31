from textnode import TextNode, TextType
from re import findall


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    out = []

    for node in old_nodes:
        if not node.text_type == TextType.TEXT:
            out.append(node)
            continue

        bits = node.text.split(delimiter)

        if len(bits) % 2 == 0:
            raise Exception("No closing tag found: " + str(bits))

        if len(bits) == 1:
            out.append(TextNode(bits[0], TextType.TEXT))
            continue

        new_nodes = []

        i = 0
        for bit in bits:
            if bit != '':
                if i % 2 == 0:
                    new_nodes.append(TextNode(bit, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(bit,text_type))

            i += 1
        out.extend(new_nodes)

    return out


def extract_markdown_images(text: str) -> list:
    regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"

    matches = findall(regex, text)

    return matches

def extract_markdown_links(text: str) -> list:
    regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"

    matches = findall(regex, text)

    return matches

# Hand Done Attempt
# def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
#     out = []
#
#     for node in old_nodes:
#         links = extract_markdown_images(node.text)
#
#         if len(links) < 1:
#             out.append(TextNode(node.text, TextType.TEXT))
#             continue
#
#         sections = [node.text.split(f"![{links[0][0]}]({links[0][1]})", 1)]
#
#         i = 1;
#         while i < len(links):
#             alt = links[i][0]
#             link = links[i][1]
#
#             sections.append(sections[i - 1][1].split(f"![{alt}]({link})", 1))
#
#             i += 1
#
#         chunks = [];
#         sections = [item for sublist in sections for item in sublist]
#
#         for section in sections:
#             if "](" not in section:
#                 chunks.append(section)
#
#         i = 0
#
#         while i < max(len(chunks), len(links)):
#             if chunks[i] and chunks[i] != '':
#                 out.append(TextNode(chunks[i], TextType.TEXT))
#             if (0 <= i < len(links)) and links[i][0] != '':
#                 out.append(TextNode(links[i][0], TextType.IMAGE, links[i][1]))
#
#             i += 1
#
#         return out
#
#
#
#
# def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
#     out = []
#
#     for node in old_nodes:
#         links = extract_markdown_links(node.text)
#
#         if len(links) < 1:
#             out.append(TextNode(node.text, TextType.TEXT))
#             continue
#
#         sections = [node.text.split(f"[{links[0][0]}]({links[0][1]})", 1)]
#
#         i = 1;
#         while i < len(links):
#             alt = links[i][0]
#             link = links[i][1]
#
#             sections.append(sections[i - 1][1].split(f"[{alt}]({link})", 1))
#
#             i += 1
#
#         chunks = [];
#         sections = [item for sublist in sections for item in sublist]
#
#         for section in sections:
#             if "](" not in section:
#                 chunks.append(section)
#
#         i = 0
#
#         while i < max(len(chunks), len(links)):
#             if chunks[i] and chunks[i] != '':
#                 out.append(TextNode(chunks[i], TextType.TEXT))
#             if (0 <= i < len(links)) and links[i][0] != '':
#                 out.append(TextNode(links[i][0], TextType.LINK, links[i][1]))
#
#             i += 1
#
#         return out

# Assisted Functions
def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    out = []

    for node in old_nodes:
        original = node.text;
        links = extract_markdown_images(original)

        if node.text_type != TextType.TEXT:
            out.append(node)
            continue

        if len(links) < 1:
            out.append(TextNode(original, TextType.TEXT))
            continue

        for link in links:
            before, after = original.split(f"![{link[0]}]({link[1]})", 1)

            if before != '':
                out.append(TextNode(before, TextType.TEXT))

            out.append(TextNode(link[0], TextType.IMAGE, link[1]))

            original = after

        if original != '':
            out.append(TextNode(original, TextType.TEXT))

    return out

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    out = []

    for node in old_nodes:
        original = node.text;
        links = extract_markdown_links(original)

        if node.text_type != TextType.TEXT:
            out.append(node)
            continue

        if len(links) < 1:
            out.append(TextNode(original, TextType.TEXT))
            continue

        for link in links:
            before, after = original.split(f"[{link[0]}]({link[1]})", 1)

            if before != '':
                out.append(TextNode(before, TextType.TEXT))

            out.append(TextNode(link[0], TextType.LINK, link[1]))

            original = after

        if original != '':
            out.append(TextNode(original, TextType.TEXT))

    return out

def text_to_textnodes(text: str) -> list[TextNode]:
    out = []

    nodes = split_nodes_delimiter([TextNode(text, TextType.TEXT)], "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)


    return nodes

