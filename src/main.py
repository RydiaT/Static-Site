from textnode import TextNode, TextType

def main():
    dummy = TextNode("yes", TextType.LINK, "www.youtube.com")

    print(dummy)

main()