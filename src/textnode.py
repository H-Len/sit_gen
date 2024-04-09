from htmlnode import LeafNode

class TextNode:
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
            return LeafNode(text_node.text)
        elif text_node.text_type == "bold":
            return LeafNode("b", text_node.text)
        elif text_node.text_type == "italic":
            return LeafNode("i", text_node.text)
            # text_type_italic: "i" tag, text
        elif text_node.text_type == "code":
            return LeafNode(text_node.tag, text_node.text)
        elif text_node.text_type == "link":
            props = {"href": text_node.url}
            return LeafNode("a", text_node.text, props)
        elif text_node.text_type == "image":
            props_src_alt = {"src": text_node.url,
                             "alt": text_node.text}
            return LeafNode("img", '', props_src_alt)
        else:
            raise Exception("Not of the available text_types")
        

trial_1 = TextNode(text="something", text_type="bold")

print(TextNode.text_node_to_html_node(trial_1))