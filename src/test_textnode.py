import unittest

from textnode import TextNode
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")

        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", "bold")
        node4 = TextNode("This is a text node", "italic")

        self.assertNotEqual(node, node4)


    def test_text_to_html(self):
        trial_1 = TextNode(text="something", text_type="bold")
        trial_1_conv = str(TextNode.text_node_to_html_node(trial_1))
        result_1 = 'b, something, None, None'
        self.assertEqual(trial_1_conv, result_1)

if __name__ == "__main__":
    unittest.main()
