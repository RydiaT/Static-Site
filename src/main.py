from textnode import TextType, TextNode


def main():
    test = TextNode("Anchor Text", TextType("LINK"), "bullshit link")

    print(test)

main()