


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def countNonLeafNode(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 0
        else:
            return 1 + self.countNonLeafNode(root.left) + self.countNonLeafNode(root.right)

    def countLeafNode(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        else:
            return self.countLeafNode(root.left) + self.countLeafNode(root.right)

    def bottomViewLeftToRight(self, root):
        if root == None:
            return
        if root.left == None and root.right == None:
            print root.data,
            return
        else:
            self.bottomViewLeftToRight(root.left)
            self.bottomViewLeftToRight(root.right)

    def getLevelOfNode(self, root, key, level=1):
        if root == None:
            return 0
        if root.data == key:
            return level
        return self.getLevelOfNode(root.left, key, level+1) or self.getLevelOfNode(root.right, key, level+1)
