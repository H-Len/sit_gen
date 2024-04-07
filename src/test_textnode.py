import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        node3 = TextNode("This is a text node", "bold", None)
        node4 = TextNode("This is a text node", "italic")

        self.assertEqual(node, node2)
        self.assertEqual(node, node3)
        self.assertEqual(node, node4)
        self.assertEqual(node2, node3)
        self.assertEqual(node2, node4)

if __name__ == "__main__":
    unittest.main()
