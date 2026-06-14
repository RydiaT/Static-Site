from enum import Enum


class TextType(Enum):
    TEXT = "TEXT"
    BOLD = "BOLD"
    ITALIC = "ITALIC"
    CODE = "CODE"
    LINK = "LINK"
    IMAGE = "IMAGE"


class TextNode:
    """
    Lowest Level Node.

    :param text: Element InnerHTML
    :type text: str
    :param text_type: Element Formatting (See TextType Enum)
    :type text_type: TextType
    :param url: Element URL (optional)
    :type url: str
    """
    def __init__(self, text: str, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"