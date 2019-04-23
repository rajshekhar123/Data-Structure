

class Node:
    """
    A node binary class
    """
    def __init__(self, data):
        """
        init method to initialise values
        """
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    """
    A binary tree class
    """
    def __init__(self):
        self.root = root

    def distance_two_node(self, root, n1 , n2):
        """
        Disatnce between two node of a  tree
        """
        if root == None:
            return None
        if root.data == n1 or root.data == n2:
            return root
        left = self.distance_two_node(root.left, n1 , n2)
        right = self.distance_two_node(root.right, n1, n2)
        if left!=None and right!=None:
            return root


