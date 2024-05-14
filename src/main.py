from textnode import TextNode
from leafnode import LeafNode


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case "text":
            return LeafNode(value=text_node.text)
        case "bold":
            return LeafNode(tag="b", value=text_node.text)
        case "italic":
            return LeafNode(tag="i", value=text_node.text)
        case "code":
            return LeafNode(tag="code", value=text_node.text)
        case "link":
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case "image":
            return LeafNode(tag="img", props={"src": text_node.url, "alt": text_node.text})
        
    raise Exception("Unexpected Type")


text_type_text = "text"
text_type_code = "code"
text_type_bold = "bold"
text_type_italic = "italic"      

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
        else:
            splitted = node.text.split(delimiter)
            if len(splitted) % 2 != 0:
                raise Exception("Unclosed delimiter")
            for index, part in enumerate (splitted):
                if index % 2 == 0:
                    new_nodes.append(TextNode(part, node.text_type))
                else:
                    new_nodes.append(TextNode(part, text_type))
    return new_nodes


def main():
    first = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(first)

main()
