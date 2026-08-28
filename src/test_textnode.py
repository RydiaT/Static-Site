import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_nourl_uneql(self):
        node = TextNode("This is a text node", TextType.BOLD, "youtube.com")
        node2 = TextNode("This is a text node", TextType.BOLD)

        self.assertNotEqual(node, node2)

    def test_diff_type(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)

        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is an IMAGE", TextType.IMAGE, "rotating_chip.gif")
        exp_result = 'TextNode(This is an IMAGE, 4, rotating_chip.gif)'

        self.assertEqual(node.__repr__(), exp_result)

    def test_repr_nourl(self):
        node = TextNode("This is an IMAGE", TextType.IMAGE)
        exp_result = 'TextNode(This is an IMAGE, 4, NO URL)'

        self.assertEqual(node.__repr__(), exp_result)

if __name__ == "__main__":
    unittest.main()