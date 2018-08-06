class Node():
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        return serialize(self)

def serialize(node):
    if node is None:
        return "#"
    return str(node.key) + " " + serialize(node.left) + " " + serialize(node.right)

def deserialize(node_str):
    tokens = node_str.split(" ")
    def parse(tokens):
        if tokens[0] == '#':
            tokens.pop(0)
            return None
        new_node = Node(tokens.pop(0))
        new_node.left = parse(tokens)
        new_node.right = parse(tokens)
        return new_node
    return parse(tokens)

if __name__ == '__main__':
    test = Node(5, Node(6, Node(1, Node(2), Node(3))),
            Node(7, Node(8)))
    print(serialize(test))
    print(str(deserialize(serialize(test))))
