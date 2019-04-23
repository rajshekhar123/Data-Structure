



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def printleft(self, root):
        if root.left == None:
            return
        print root.data,
        self.printleft(root.left)

    def printright(self, root):
        if root.right == None:
            return
        self.printright(root.right)
        print root.data,

    def printleaves(self, root):
        if root == None:
            return
        if root.left == None and root.right == None:
            print root.data,
        self.printleaves(root.left)
        self.printleaves(root.right)

    def boundaryLevelTraversal(self):
        """
        Traverse the left travel leaves travel right
        """
        self.printleft(self.root)
        self.printleaves(self.root)
        self.printright(self.root.right)
