class HTMLNode:
    def __init__(self, tag: str | None = None, value: str | None = None, children: list["HTMLNode"] | None = None, props: dict[str, str] | None =  None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props is None:
            return ''

        out = ""

        if self.props:
            for key, value in self.props.items():
                out += f' {key}="{value}"'

        return out

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict[str, str] | None = None):
        super().__init__(tag, value, props=props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError("Value is blank. Leaf Nodes MUST have a value.")

        if not self.tag:
            return f"{self.value}"

        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"