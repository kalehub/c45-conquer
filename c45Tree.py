# a file to build the tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, data):
        self.root = Node(data)

    def print_tree(self, root):
        if root:
            print(root.data)
