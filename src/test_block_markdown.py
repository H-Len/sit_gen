import unittest

from block_markdown import markdown_to_blocks

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

if __name__ == "__main__":
    unittest.main()