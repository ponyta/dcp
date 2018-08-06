class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

# returns the height of the root if balanced
# otherwise returns false
def height_balanced(root):
    if root is None:
        return 0
    left_height = height_balanced(root.left)
    right_height = height_balanced(root.right)
    if left_height is False:
        return False
    if right_height is False:
        return False
    if abs(right_height - left_height) > 1:
        return False
    return max(right_height, left_height) + 1

if __name__ == '__main__':
    test_tree = Node(5, Node(6, Node(1, Node(0), None), Node(2)),
            Node(9))
    print(height_balanced(test_tree))
