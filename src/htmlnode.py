

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        for key in self.props:
            result += f'''{key}="{self.props[key]}" '''
        return result.strip()

    def __repr__(self):
        return f"HTMLNode(\ntag={self.tag},\nvalue={self.value},\nchildren={self.children},\nprops={self.props_to_html()}\n)"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return self.value
        if self.props:
            return f"<{self.tag} "+ f"{self.props_to_html()}>" + f"{self.value}" + f"</{self.tag}>"
        return f"<{self.tag}>" + f"{self.value}" + f"</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError
        if not self.children:
            raise ValueError("missing children")
        
        node = ""
        if self.props:
            node = f"<{self.tag} {self.props_to_html()}>"
        else:
            node = f"<{self.tag}>"
        for child in self.children:
            node += child.to_html()

        node += f"</{self.tag}>"
        return node