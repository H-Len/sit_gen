import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        new_node = HTMLNode("<a>", "The start of things", None, {"start": "begin", "finish": "end"})

        self.assertEqual(new_node.props_to_html(), ' start="begin" finish="end"')

    def test_to_html(self):
        one_leaf = LeafNode("p", "This is a paragraph of text.")
        two_leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        parent_n = ParentNode("div", [one_leaf, two_leaf], None)

        self.assertEqual(parent_n.to_html(), '<div><p>This is a paragraph of text.</p><a href="https://www.google.com">Click me!</a></div>')

if __name__ == "__main__":
    unittest.main()