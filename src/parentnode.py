from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, children, tag=None, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag Required")
        if not self.children:
            raise ValueError("Children Required")
        
        total = ""
        
        for child in self.children:
            total += child.to_html()

        return f"<{self.tag}>{total}</{self.tag}>"



        



