class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        propstring = ''
        if self.props:
            for k, v in self.props.items():
                propstring += f" {k}=\"{v}\""
        return propstring
    def __repr__(self):
        return f"HTMLNode({tag}, {value}, {children}, {props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Invalid HTML: leadnode with no value")
        if self.tag == None:
            return str(self.value)
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props=None)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Invalid HTML: parentnode with no tag")
        if self.children == None:
            raise ValueError("Invalid HTML: parentnode with no children")
        htmlstring = ''
        for child in self.children:
            htmlstring += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{htmlstring}</{self.tag}>"
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
                
    