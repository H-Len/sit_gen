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

def block_to_block_type(blocks):
    # '''I recommend creating variables that represent each block type and importing them wherever you need to use them, e.g. block_type_paragraph = "paragraph".

    # -Headings start with 1-6 # characters, followed by a space and then the heading  text.
    # -Code blocks must start with 3 backticks and end with 3 backticks.
    # -Every line in a quote block must start with a > character.
    # -Every line in an unordered list block must start with a * or - character, followed by a space.
    # -Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
    # -If none of the above conditions are met, the block is a normal paragraph.'''

    block_type_heading = "heading"
    block_type_code = "code"
    block_type_quote = "quote"
    block_type_unordered = "unordered list"
    block_type_ordered = "ordered list"
    block_type_paragraph = "paragraph"
    i = 0
    hash = 0
    block_type = ""


    lines = blocks.split('\n')
    for line in lines:
        i = 0
        hash = 0
        block_type = ""
        for char in line:
            if char == "#":
                hash += 1
                i += 1
        if hash != 0 and line[hash] == ' ':
            # i += 1
            block_type = block_type_heading
            return block_type
        i = 0
        line_len = len(line)
        if line[i: 3] == '```' and line[-3: line_len] == '```':
            block_type = block_type_code
            return block_type
        elif line[0] == '>':
            block_type = block_type_quote
        elif line[0] == '-' or line[0] == '*':
            block_type = block_type_unordered
        elif re.match(r"^\d+\.", line):
            block_type = block_type_ordered
        else:
            block_type = block_type_paragraph

        return block_type