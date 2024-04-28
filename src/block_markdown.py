import re

markdown_text = "This is **bolded** paragraph\n"\
"\n"\
"This is another paragraph with *italic* text and `code` here \n"\
"This is the same paragraph on a new line \n"\
"\n"\
"* This is a list \n"\
"* with items"

# print(markdown_text)

def markdown_to_blocks(markdown):
    blocks = re.split(r'\n+', markdown)
    print(blocks)