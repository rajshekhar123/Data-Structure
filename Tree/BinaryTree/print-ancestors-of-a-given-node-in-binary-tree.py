


class Node:
    """
    class Node
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    """
    class binary tree
    """
    def __init__(self):
        self.root = None

    def printAncestor(self, root, n1):
        """
        Print the ancestor of a binary tree
        """
        if root == None:
            return False
        if root.data == n1:
            return True
        if self.printAncestor(root.left, n1) or self.printAncestor(root.right, n1):
            print root.data,
            return True
        return False
