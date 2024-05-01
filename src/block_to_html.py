import re
from textnode import TextNode
from htmlnode import HTMLNode
from block_markdown import markdown_to_blocks, block_to_block_type

def blocktype_to_html(blocks):
    block_type_heading = "heading"
    block_type_code = "code"
    block_type_quote = "quote"
    block_type_unordered = "unordered list"
    block_type_ordered = "ordered list"
    block_type_paragraph = "paragraph"
    for block in blocks:
        if block_to_block_type(block) == block_type_heading:
            # Headings should be surrounded by a <h1> to <h6> tag, depending on the number of # characters.
            count = 0
            if count('#') == 2:
                split_block = block.split('#')
                return f"<h1>{split_block}</h1>"
            elif count('##') == 2:
                split_block = block.split('##')
                return f"<h2>{split_block}</h2>"
            elif count('###') == 2:
                split_block = block.split('###')
                return f"<h3>{split_block}</h3>"
            elif count('####') == 2:
                split_block = block.split('####')
                return f"<h4>{split_block}</h4>"
            elif count('#####') == 2:
                split_block = block.split('#####')
                return f"<h5>{split_block}</h5>"
            elif count('######') == 2:
                split_block = block.split('######')
                return f"<h6>{split_block}</h6>"
        
        elif block_to_block_type(block) == block_type_ordered:
            # Ordered list blocks should be surrounded by a <ol> tag, and each list item should be surrounded by a <li> tag.
            ol_string = '''1. good morning
            2. good afternoon
            3. good night'''
            html_ol = f"<ol>{ol_string}<ol>"
        
        elif block_to_block_type(block) == block_type_quote:
            #tentative skeleton:
            # Quote blocks should be surrounded by a <blockquote> tag.
            quote_string = '>hello'
            return f"<blockquote>{quote_string}</blockquote>"

        elif block_to_block_type(block) == block_type_unordered:
            # Unordered list blocks should be surrounded by a <ul> tag, and each list item should be surrounded by a <li> tag.
            ul_string = '''* sleep better
            * wake refreshed'''
            new_ul = ['<ul> ']
            split_ul = ul_string.split('*')
            for line in split_ul:
                new_ul.append(f'<li>line</li>')
            ''.join(new_ul)
            new_ul.append('</ul>')
            return f"{new_ul}"


        elif block_to_block_type(block) == block_type_code:
            # Code blocks should be surrounded by a <code> tag nested inside a <pre> tag.
            return f"<pre><code>{block}</code></pre>"

        elif block_to_block_type(block) == block_type_paragraph:
            # Paragraphs should be surrounded by a <p> tag.
            return f"<p>{block}</p>"

block = '* smile'

print(blocktype_to_html(block))