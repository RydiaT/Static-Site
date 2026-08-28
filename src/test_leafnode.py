import unittest
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        result = "LeafNode(a, Click me!, {'href': 'https://www.google.com'})"

        self.assertEqual(node.__repr__(), result)

    def test_to_html_p(self):
        node = LeafNode("p", "This is a paragraph of text.")
        result = "<p>This is a paragraph of text.</p>"

        self.assertEqual(node.to_html(), result)

    def test_to_html_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        result = '<a href="https://www.google.com">Click me!</a>'

        self.assertEqual(node.to_html(), result)

    def test_to_html_styled_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "style": "color: red;"})
        result = '<a href="https://www.google.com" style="color: red;">Click me!</a>'

        self.assertEqual(node.to_html(), result)

if __name__ == "__main__":
    unittest.main()