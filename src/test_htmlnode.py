import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        new_node = HTMLNode("<a>", "The start of things", None, {"start": "begin", "finish": "end"})

        print(new_node.props_to_html())

        self.assertEqual(new_node.props_to_html(), ' start="begin" finish="end"')

    def test_to_html(self):
        one_leaf = LeafNode("p", "This is a paragraph of text.")
        two_leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        print(one_leaf.to_html())
        print(two_leaf.to_html())

if __name__ == "__main__":
    unittest.main()