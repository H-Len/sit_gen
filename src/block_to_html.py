import re
from textnode import TextNode
from htmlnode import HTMLNode
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link
from block_markdown import markdown_to_blocks, block_to_block_type

def blocktype_to_html(blocks):
    block_type_heading = "heading"
    block_type_code = "code"
    block_type_quote = "quote"
    block_type_unordered = "unordered list"
    block_type_ordered = "ordered list"
    block_type_paragraph = "paragraph"
    current_block_type = block_to_block_type(blocks)
    # for block in blocks:
    if current_block_type == block_type_heading:
        count = 0
        for char in blocks[0:6]:
            if char == '#':
                count += 1
        return f"<h{count}>{blocks[count+1:]}</h{count}>"
        
    elif block_to_block_type(blocks) == block_type_code:
        # Code blocks should be surrounded by a <code> tag nested inside a <pre> tag.
        stript_blocks = blocks[3:-3]
        return f"<pre><code>{stript_blocks}</code></pre>"
    
    elif block_to_block_type(blocks) == block_type_quote:
        # Quote blocks should be surrounded by a <blockquote> tag.
        block_lines = blocks.split('\n')
        clean_lines = []
        for line in block_lines:
            new_line = line.lstrip('> ')
            clean_lines.append(new_line)
        new_block = '\n'.join(clean_lines)
        return f"<blockquote>{new_block}</blockquote>"

    elif block_to_block_type(blocks) == block_type_unordered:
        # Unordered list blocks should be surrounded by a <ul> tag, and each list item should be surrounded by a <li> tag.
#         ul_string = '''* sleep better 
# * wake refreshed'''
        new_ul = ['<ul>']
        split_ul = blocks.split('- ')
        for line in split_ul:
            clean_line = line.rstrip('\n')
            if clean_line != '':               
                new_ul.append(f'<li>{clean_line}</li>')
        ''.join(new_ul)
        new_ul.append(f'</ul>')
        return f"{''.join(new_ul)}"
    
    elif current_block_type == block_type_ordered:
        # Ordered list blocks should be surrounded by a <ol> tag, and each list item should be surrounded by a <li> tag.
#         ol_string = '''1. good morning
# 2. good afternoon
# 3. good night'''
        new_ol = ['<ol>']
        split_ol = blocks.split("\n")

        ol_instances = re.findall(r"^\d+\. ", blocks, re.MULTILINE)
        ol_lines = []
        for i in ol_instances:
            instance = i.strip(re.match(r"^\d+\. ", ol_instances))
            ol_lines.append(instance)
        print(ol_lines)
        for line in split_ol:
            clean_line = line.rstrip('\n')
            if clean_line != '':
                new_ol.append(f'<li>{clean_line}</li>')
        ''.join(new_ol)
        new_ol.append('</ol>')
        return f"{''.join(new_ol)}"

    elif block_to_block_type(blocks) == block_type_paragraph:
        # Paragraphs should be surrounded by a <p> tag.
        return f"<p>{blocks}</p>"

        

heading_test = '## hi'

def test_heading(self):
    print(blocktype_to_html(heading_test))