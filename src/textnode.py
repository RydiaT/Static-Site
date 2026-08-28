from enum import Enum


class TextType(Enum):
    TEXT = 0
    ITALIC = 1
    CODE = 2
    LINK = 3
    IMAGE = 4

class TextNode():
    def __init__(self, text: str, text_type: TextType, url: str):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"