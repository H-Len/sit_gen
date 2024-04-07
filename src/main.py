from textnode import TextNode


new_node = TextNode('some new string', 'bold', 'https://here.go')
other_node = TextNode('stringing chars here', 'bold', 'www.here.now')

def main():
    print(new_node.__eq__(other_node))
    new_node.__repr__()
    other_node.__repr__()

    print(new_node.__repr__())
    print(other_node.__repr__())

main()