import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_level_one(self):
        node = ParentNode(
            tag="p",
            children=[
                LeafNode(tag="b", value="This is bold"),
                LeafNode(value=" and this is not")
            ]
        )
        self.assertEqual("<p><b>This is bold</b> and this is not</p>", node.to_html())

    def test_level_two(self):
        node = ParentNode(
            tag="div",
            children=[
                ParentNode(
                    tag="ul",
                    children=[
                        LeafNode(tag="li", value="Item 1"),
                        LeafNode(tag="li", value="Item 2"),
                        ParentNode(
                            tag="li",
                            children=[
                                ParentNode(
                                    tag="p",
                                    children=[LeafNode(value="Nested paragraph in list")]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.assertEqual("<div><ul><li>Item 1</li><li>Item 2</li><li><p>Nested paragraph in list</p></li></ul></div>", node.to_html())

    def test_siblings_deeper(self):
        node = ParentNode(
            tag="section",
            children=[
                LeafNode(tag="h1", value="Heading"),
                ParentNode(
                    tag="p",
                    children=[
                        LeafNode(value="A paragraph with "),
                        LeafNode(tag="em", value="emphasized text"),
                        LeafNode(value=" in the middle.")
                    ]
                ),
                LeafNode(tag="p", value="Another paragraph.")
            ]
        )
        self.assertEqual("<section><h1>Heading</h1><p>A paragraph with <em>emphasized text</em> in the middle.</p><p>Another paragraph.</p></section>", node.to_html())

    def test_missing_tag(self):
        with self.assertRaises(ValueError) as cm:
            ParentNode(children=[LeafNode(value="Child")]).to_html()
        self.assertEqual(str(cm.exception), "Tag Required")

    def test_missing_children(self):
        with self.assertRaises(ValueError) as cm:
            ParentNode(tag="div", children=[]).to_html()
        self.assertEqual(str(cm.exception), "Children Required")

if __name__ == "__main__":
    unittest.main()