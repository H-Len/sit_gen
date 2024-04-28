import unittest

from block_markdown import markdown_to_blocks

def test_markdown_to_blocks(self):
    markdown_text = "This is **bolded** paragraph\n"\
    "\n"\
    "This is another paragraph with *italic* text and `code` here \n"\
    "This is the same paragraph on a new line \n"\
    "\n"\
    "* This is a list \n"\
    "* with items"
    blocks = markdown_to_blocks(markdown_text)

    print(blocks)