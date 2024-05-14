from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props )

    def to_html(self):
        if self.value == None and not self.tag == "img":
            raise ValueError("LeafNode requires a value.")
        if self.tag == None:
            return self.value
        
        prop = ""
        if self.props:
            prop = " " + self.props_to_html()

        return f'<{self.tag}{prop}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
