import unittest
from textnode import TextNode, TextType
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("a", "Testy McTesterson", [HTMLNode("b", "Boldy McBolderson")], {"style": "color: red;"})
        exp_repr = "HTMLNode(a, Testy McTesterson, [HTMLNode(b, Boldy McBolderson, None, None)], {'style': 'color: red;'})"

        self.assertEqual(node.__repr__(), exp_repr)

    def test_props_to_html_one(self):
        node = HTMLNode(props={"style": "color: red;"})
        result = 'style="color: red;"'

        self.assertEqual(node.props_to_html(), result)

    def test_props_to_html_two(self):
        node = HTMLNode(props={"style": "color: red;", "href": "youtube.com"})
        result = 'style="color: red;" href="youtube.com"'

        self.assertEqual(node.props_to_html(), result)

    def test_props_to_html_zero(self):
        node = HTMLNode(props={})
        result = ''

        self.assertEqual(node.props_to_html(), result)

if __name__ == "__main__":
    unittest.main()