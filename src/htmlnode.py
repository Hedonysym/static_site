from functools import reduce

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented for parent class, sorry :(")
    
    def props_to_html(self):
        items = []
        output = ""
        for key in self.props:
            items.append(f' {key}=\"{self.props[key]}\"')
        for item in items:
            output = output + item
        return output
    
    def __repr__(self):
        return f"HTMLNode contains: {self.tag}, {self.value}, {self.children}, {self.props}"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode must have string value")
        elif self.tag == None:
            return self.value
        elif self.props == None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.children == None:
            raise ValueError("ParentNode must have children value")
        elif self.tag == None:
            raise ValueError("ParentNode must have tag value")
        return f'<{self.tag}>{"".join(map(lambda node: node.to_html(), self.children))}</{self.tag}>'
    
