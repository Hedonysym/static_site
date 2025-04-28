
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
