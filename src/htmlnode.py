class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        p2html = []
        if self.props == None:
            return ""
        for k,v in self.props.items():
            p2html.append(f' {k}="{v}"')
        return ''.join(p2html)

    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        if self.value == None:
            raise ValueError("Invalid: no value!")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

def main():
    a_node = HTMLNode("<a>", value = "Hello, there", children = None, props = {"href": "https://www.google.com", "target": "_blank"})
    
    # print(a_node.props_to_html())
    # print(a_node.__repr__())
    # print(a_node.props.keys())
    leaf_node1 = LeafNode("a", "Hi", {"href": "try.me.com", "target": "_blank"})
    print(leaf_node1.to_html())
main()