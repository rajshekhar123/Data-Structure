


class Node:
    """
    Used while creating a node
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    """
    Class containing all the major definations
    """

    def __init__(self):
        self.root = None

    def lca(self, root, n1, n2):
        """
        Lowest common ancestor of two nodes
        """
        if root == None:
            return None
        if root.data == n1 or root.data == n2:
            return root
        left = self.lca(root.left, n1, n2)
        right = self.lca(root.right, n1, n2)
        if left!=None and right!=None:
            return root
        if left == None and right == None:
            return None
        return left if left!=None else right


