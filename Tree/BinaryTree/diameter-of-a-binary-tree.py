


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):
        self.root = None

    def height(self, root):
        if root == None:
            return 0
        hleft = self.height(root.left)
        hright = self.height(root.right)
        if hleft>hright:
            return 1 + hleft
        else:
            return 1 + hright

    def diameterOfTree(self, root):
        h1 = self.height(root.left)
        h2 = self.height(root.right)
        print h1 + 1 + h2
