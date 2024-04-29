import re

markdown_text = '''This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
'''


def markdown_to_blocks(markdown_text):
    blocks = [] 
    sections = markdown_text.split('\n\n')
    for s in sections:
        if s != '':
            trim_s = s.strip()
            blocks.append(trim_s)
    return blocks

markdown_to_blocks(markdown_text)