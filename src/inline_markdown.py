import re
from textnode import TextNode
from htmlnode import HTMLNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextNode.text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextNode.text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextNode.text_type_text:
            new_nodes.append(old_node)
            continue
        extract_nodes = extract_markdown_images(old_node.text)
        if extract_nodes != []:
            alt, url = extract_nodes[0]
            sections = old_node.text.split(f"![{alt}]({url})", 1)
            new_nodes.append(TextNode(sections[0], TextNode.text_type_text))
            new_nodes.append(TextNode(alt, TextNode.text_type_image, url))
            if sections[1] != "":
                new_nodes.extend(split_nodes_image([TextNode(sections[1], TextNode.text_type_text)]))
        else:
            new_nodes.append(TextNode(old_node.text, TextNode.text_type_text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextNode.text_type_text:
            new_nodes.append(old_node)
            continue
        extract_nodes = extract_markdown_links(old_node.text)
        if extract_nodes != []:
            link_text, url = extract_nodes[0]
            sections = old_node.text.split(f"[{link_text}]({url})", 1)
            new_nodes.append(TextNode(sections[0], TextNode.text_type_text))
            new_nodes.append(TextNode(link_text, TextNode.text_type_link, url))
            if sections[1] != "":
                new_nodes.extend(split_nodes_link([TextNode(sections[1], TextNode.text_type_text)]))
        else:
            new_nodes.append(TextNode(old_node.text, TextNode.text_type_text))
    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def text_to_textnodes(text):
    new_nodes = []