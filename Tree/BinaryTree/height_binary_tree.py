

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def height(self, root):
        """
        calculates height of binary Tree
        """
        if root == None:
            return 0
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        if lheight>rheight:
            return 1+lheight
        else:
            return 1+rheight

