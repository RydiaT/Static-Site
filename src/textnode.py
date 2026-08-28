from enum import Enum


class TextType(Enum):
    TEXT = 0
    ITALIC = 1
    CODE = 2
    LINK = 3
    IMAGE = 4
    BOLD = 5

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = "NO URL"):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TextNode):
            raise TypeError(f"other must be instance of TextNode, got {type(other)}")

        return (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"