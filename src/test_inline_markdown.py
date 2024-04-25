import unittest
from inline_markdown import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link
)

from textnode import (
    TextNode
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextNode.text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", TextNode.text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextNode.text_type_text),
                TextNode("bolded", TextNode.text_type_bold),
                TextNode(" word", TextNode.text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextNode.text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", TextNode.text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextNode.text_type_text),
                TextNode("bolded", TextNode.text_type_bold),
                TextNode(" word and ", TextNode.text_type_text),
                TextNode("another", TextNode.text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextNode.text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", TextNode.text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextNode.text_type_text),
                TextNode("bolded word", TextNode.text_type_bold),
                TextNode(" and ", TextNode.text_type_text),
                TextNode("another", TextNode.text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextNode.text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", TextNode.text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextNode.text_type_text),
                TextNode("italic", TextNode.text_type_italic),
                TextNode(" word", TextNode.text_type_text),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextNode.text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", TextNode.text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextNode.text_type_text),
                TextNode("code block", TextNode.text_type_code),
                TextNode(" word", TextNode.text_type_text),
            ],
            new_nodes,
        )

    def test_img(self):
        node = TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
        TextNode.text_type_text,
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("This is text with an ", TextNode.text_type_text),
                TextNode("image", TextNode.text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and another ", TextNode.text_type_text),
                TextNode(
                    "second image", TextNode.text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
                ),
            ]

        , new_nodes)

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextNode.text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
                TextNode(" and ", text_type_text),
                TextNode("another link", text_type_link, "https://blog.boot.dev"),
                TextNode(" with text that follows", text_type_text),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()