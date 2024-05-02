import unittest

from block_to_html import blocktype_to_html
# block = '* smile'

# print(blocktype_to_html(block))

class TestInlineMarkdown(unittest.TestCase):
    def test_header(self):
        heading_test = '### hi'
        expected_heading = '<h3>hi</h3>'
        h_test = blocktype_to_html(heading_test)
        self.assertEqual(h_test, expected_heading)
    def test_code(self):
        code_test = '```something```'
        expected_code = '<pre><code>something</code></pre>'
        self.assertEqual(blocktype_to_html(code_test), expected_code)
    def test_quote(self, quote_test):
        quote_test = '''> the beginning
> is here'''
        expected_quote = '<blockquote> the beginning\n is here</blockquote>'
        self.assertEqual(blocktype_to_html(quote_test), expected_quote)
    def test_ul(self):
        unordered_test = '''- pack
- move'''
        expected_ul = '''<ul>
    <li>pack</li>
    <li>move</li>
</ul>'''
        print(blocktype_to_html(unordered_test))
    def test_ol(self):
        ordered_test = '''1. wake up
2. smile'''
        espected_ol = '''<ol>
            <li>wake up</li>
            <li>smile</li>
        </ol>'''
        print(blocktype_to_html(ordered_test))
    def test_paragraph(self):
        paragraph_test = '''I originally thought something for the first time and it was just me, myself, who thought it.
        But, then I told you, and you thought about it, too.
        Still original?
        '''
        expected_p = '''<p>I originally thought something for the first time and it was just me, myself, who thought it.
        But, then I told you, and you thought about it, too.
        Still original?</p>'''

        print(blocktype_to_html(paragraph_test))

    # def test_markdown_to_blocks(self):
    #     heading_test = '### hi'
    #     expected_heading = '<h3>hi</h3>'
    #     code_test = '```something```'
    #     expected_code = '<pre><code>something</code></pre>'
    #     quote_test = '''> the beginning
    #     > is here'''
    #     expected_quote = '<blockquote> the beginning\n is here</blockquote>'
    #     unordered_test = '''- pack
    #     - move'''
    #     ordered_test = '''1. wake up
    #     2. smile'''
    #     paragraph_test = '''I originally thought something for the first time and it was just me, myself, who thought it.
    #     But, then I told you, and you thought about it, too.
    #     Still original?
    #     '''

if __name__ == "__main__":
    unittest.main()