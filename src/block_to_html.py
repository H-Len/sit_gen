import re
from textnode import TextNode
from htmlnode import LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from block_markdown import markdown_to_blocks, block_to_block_type

class Block_type:
    block_type_heading = "heading"
    block_type_code = "code"
    block_type_quote = "quote"
    block_type_unordered = "unordered list"
    block_type_ordered = "ordered list"
    block_type_paragraph = "paragraph"

###redo returns to return an HTML node
def blocktype_to_html(blocks):

    current_block_type = block_to_block_type(blocks)
    if current_block_type == Block_type.block_type_heading:
        count = 0
        for char in blocks[0:6]:
            if char == '#':
                count += 1
        st_range = count
        # short_string = blocks]
        # new_node = LeafNode(f'h{count}', blocks[st_range:], None)
        return node_format(f'h{count}', blocks[st_range:])
        
    elif current_block_type == Block_type.block_type_code:
        # Code blocks should be surrounded by a <code> tag nested inside a <pre> tag.
        stript_blocks = blocks[3:-3]
        # return f"<pre><code>{stript_blocks}</code></pre>"
        code_node = LeafNode('code', stript_blocks, None)
        return ParentNode('pre', [code_node], None)
    
    elif current_block_type == Block_type.block_type_quote:
        # Quote blocks should be surrounded by a <blockquote> tag.
        block_lines = blocks.split('\n')
        clean_lines = []
        for line in block_lines:
            new_line = line.lstrip('> ')
            clean_lines.append(new_line)
        new_block = '\n'.join(clean_lines)
        return LeafNode('blockquote', new_block, None)

    elif current_block_type == Block_type.block_type_unordered:
        # Unordered list blocks should be surrounded by a <ul> tag, and each list 
        new_ul = []
        split_ul = blocks.split('- ')
        for line in split_ul:
            clean_line = line.rstrip('\n')
            if clean_line != '':               
                new_ul.append(node_format('li', clean_line))

        return ParentNode('ul', new_ul, None)
    
    elif current_block_type == Block_type.block_type_ordered:
        # Ordered list blocks should be surrounded by a <ol> tag, and each list item should be surrounded by a <li> tag.
        new_li = []
        ol_nums = re.findall(r"^\d+\. ", blocks, re.MULTILINE)
        rest = blocks
        for num in ol_nums:
            sections = rest.split(num, 1)
            if sections[0] != '':
                next = sections[0].rstrip('\n')
                new_li.append(node_format('li', next))
            rest = sections[1]
        new_li.append(node_format('li', rest))
        return ParentNode('ol', new_li, None)

    elif current_block_type == Block_type.block_type_paragraph:
        # Paragraphs should be surrounded by a <p> tag.
        # paragraph_components = []
        new_blocks = text_to_textnodes(blocks)
        children = []
        for node in new_blocks:
            children.append(node.text_node_to_html_node())
        return ParentNode('p', children, None)
        

        

heading_test = '## hi'

def test_heading(self):
    return blocktype_to_html(heading_test)


def extract_ol_start(blocks):
    matches = re.findall(r"^\d+\. ", blocks)
    new_block = []
    print(f'block: {blocks}')
    return matches

def node_format(tag, val):
    new_blocks = text_to_textnodes(val)
    children = []
    for node in new_blocks:
        children.append(node.text_node_to_html_node())
    return ParentNode(tag, children, None)
