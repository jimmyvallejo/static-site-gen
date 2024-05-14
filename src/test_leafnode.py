import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_value_only(self):
        node = LeafNode(value="This is a paragraph of text.")
        self.assertEqual("This is a paragraph of text.", node.to_html())
    
    def test_to_html_full(self):
       node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
       self.assertEqual('<a href="https://www.google.com">Click me!</a>', node.to_html())

    def test_to_html_full_not_equal(self):
       node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
       self.assertNotEqual('<a href="https://www.google.comm">Click me!</a>', node.to_html())
    
    def test_to_html_raises_value_error_without_value(self):
        with self.assertRaises(ValueError):
            LeafNode(tag="p")

if __name__ == "__main__":
    unittest.main()

    

