import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_ueq(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node1, node2)

    def test_ueq2(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node1", "bold")
        self.assertNotEqual(node1, node2)

    def test_eq_url(self):
        node1 = TextNode("This is a text node", "bold", "www.boot.dev")
        node2 = TextNode("This is a text node1", "bold", "www.boot.dev")
        self.assertEqual(node1.url, node2.url)

    def test_repr(self):
        node1 = TextNode("This is a text node", "bold", "www.boot.dev")
        self.assertEqual(
            "TextNode (This is a text node, bold, www.boot.dev)", repr(node1)
        )

    def test_none(self):
        node = TextNode("Test", "bold", None)
        self.assertEqual(node.url, None)
 

if __name__ == "__main__":
    unittest.main()
