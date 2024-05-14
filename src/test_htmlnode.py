import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_html_equal(self):
        node = HTMLNode("tag", "5", None, {"href": "https://www.google.com", "target": "_blank"} )
        self.assertEqual(node.props_to_html(),  'href="https://www.google.com" target="_blank"' )
    
    def test_props_html_unequal(self):
        node = HTMLNode("tag", "5", None, {"href": "https://www.google.com", "target": "_blank"} )
        self.assertNotEqual(node.props_to_html(),  'href="https://www.google.com" target="_blank2"' )
    

if __name__ == "__main__":
    unittest.main()

    

