from htmlnode import LeafNode

class TextNode:
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"

    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def text_node_to_html_node(text_node):
        if text_node.text_type == "text":
            return LeafNode(None, text_node.text)
        elif text_node.text_type == "bold":
            return LeafNode("b", text_node.text)
        elif text_node.text_type == "italic":
            return LeafNode("i", text_node.text)
            # text_type_italic: "i" tag, text
        elif text_node.text_type == "code":
            return LeafNode("code", text_node.text)
        elif text_node.text_type == "link":
            props = {"href": text_node.url}
            return LeafNode("a", text_node.text, props)
        elif text_node.text_type == "image":
            props_src_alt = {"src": text_node.url,
                             "alt": text_node.text}
            return LeafNode("img", '', props_src_alt)
        else:
            raise Exception("Not of the available text_types")
