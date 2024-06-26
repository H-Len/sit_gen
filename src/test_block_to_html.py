import unittest
import re 

from block_to_html import blocktype_to_html

class TestInlineMarkdown(unittest.TestCase):
    def test_header(self):
        heading_test = '### hi'
        expected_heading = '<h3>hi</h3>'
        h_test = blocktype_to_html(heading_test)
        return self.assertEqual(h_test, expected_heading)
    def test_code(self):
        code_test = '```something```'
        expected_code = '<pre><code>something</code></pre>'
        return self.assertEqual(blocktype_to_html(code_test), expected_code)
    def test_quote(self):
        quote_test = '''> the beginning
> is here'''
        expected_quote = '<blockquote>the beginning\nis here</blockquote>'
        return self.assertEqual(blocktype_to_html(quote_test), expected_quote)
    def test_ul(self):
        unordered_test = '''- pack
- move'''
        expected_ul = '''<ul><li>pack</li><li>move</li></ul>'''
        return self.assertEqual(blocktype_to_html(unordered_test), expected_ul)
    def test_ol(self):
        ordered_test = '''166. wake up
2. get dressed
3. smile'''
        expected_ol = '''<ol><li>wake up</li><li>get dressed</li><li>smile</li></ol>'''
        return self.assertEqual(blocktype_to_html(ordered_test), expected_ol)
   
    def test_paragraph(self):
        paragraph_test = '''I originally thought something for the first time and it
was just me, myself, who thought it.
But, then I told you, and you thought about it, too.
Still original?'''
        expected_p = '''<p>I originally thought something for the first time and it
was just me, myself, who thought it.
But, then I told you, and you thought about it, too.
Still original?</p>'''
        return self.assertEqual(blocktype_to_html(paragraph_test), expected_p)

if __name__ == "__main__":
    unittest.main()