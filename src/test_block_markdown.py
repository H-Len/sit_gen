import unittest

from block_markdown import markdown_to_blocks, block_to_block_type

class TestInlineMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown_text = '''This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
'''

        expected = ['This is **bolded** paragraph', 'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', '* This is a list\n* with items']
        blocks = markdown_to_blocks(markdown_text)

        self.assertListEqual(blocks, expected)
    
    def test_block_type(self):
        block_type_heading = "heading"
        block_type_code = "code"
        block_type_quote = "quote"
        block_type_unordered = "unordered list"
        block_type_ordered = "ordered list"
        block_type_paragraph = "paragraph"
        
        heading_test = '### hi'
        code_test = '```something```'
        quote_test = '''> the beginning
        > is here'''
        unordered_test = '''- pack
        - move'''
        ordered_test = '''1. wake up
        2. smile'''
        paragraph_test = '''I originally thought something for the first time and it was just me, myself, who thought it.
        But, then I told you, and you thought about it, too.
        Still original?
        '''

        self.assertEqual(block_to_block_type(heading_test), block_type_heading)
        self.assertEqual(block_to_block_type(code_test), block_type_code)
        self.assertEqual(block_to_block_type(quote_test), block_type_quote)
        self.assertEqual(block_to_block_type(unordered_test), block_type_unordered)
        self.assertEqual(block_to_block_type(ordered_test), block_type_ordered)
        self.assertEqual(block_to_block_type(paragraph_test), block_type_paragraph)

if __name__ == "__main__":
    unittest.main()