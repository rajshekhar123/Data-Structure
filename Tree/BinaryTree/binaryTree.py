#
# Level order traversal
# >>> a = BinaryTree()
# >>>a.root = Node(20)
# >>> a.root.left = Node(8)
# >>> a.root.right = Node(22)
# >>> a.root.left.left = Node(4)
# >>> a.root.left.right = Node(12)
# >>> a.root.left.right.left = Node(10)
# >>> a.root.left.right.right = Node(14)
# >>> a.inorder(a.root)
# 4 8 10 12 14 20 22
# >>> a.levelorderTraversal(a.root)
# 20 8 22 4 12 10 14

class Node:
    """
    This node creates a class object
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    """
    This class contains definations
    """

    def __init__(self):
        self.root = None

    def inorder(self, node):
        """
        Inorder Traversal of a binay tree
        """
        if node == None:
            return
        self.inorder(node.left)
        print node.data,
        self.inorder(node.right)

    def preorder(self, node):
        """
        Preorder Traversal
        """
        if node == None:
            return
        print node.data,
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self, node):
        """
        PostOrder Traversal
        """
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print node.data,

    def levelorderTraversal(self, node):
        """
        Level Order Traversal
        """
        import Queue
        q = Queue.Queue()
        q.put(node)
        while not q.empty():
            node = q.get()
            print node.data,
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)

    def levelorderTraversalRecusive(self, node):
        """
        Level order Traversal in recursive format
        """
        pass

    def height(self, node):
        """
        Print height of a binay tree
        the number of nodes along the longest path from the root node down to the farthest leaf node
        """

        if node == None:
            return 0
        lheight = self.height(node.left) + 1
        rheight = self.height(node.right) + 1
        if lheight>rheight:
            return lheight
        else:
            return rheight

    def spiralOrderTraversal(self, node):
        """
        Spiral order traversal of a binay tree using two stacks
        """
        s1 = []
        s2 = []
        s1.append(node)
        while s1 or s2:
            while s1:
                node = s1.pop()
                print node.data,
                if node.right:
                    s2.append(node.right)
                if node.left:
                    s2.append(node.left)
            while s2:
                node = s2.pop()
                print node.data,
                if node.left:
                    s1.append(node.left)
                if node.right:
                    s1.append(node.right)

    def levelOrderLineByLine(self, node):
        """
        Level order traversal line by line
        """
        import Queue
        q = Queue.Queue()
        q.put(node)
        while not q.empty():
            size = q.qsize()
            while size>0:
                node = q.get()
                print node.data,
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
                size = size - 1
            print

    def reverseLevelOrderTraversal(self, node):
        """
        Reverse level of traversal using queue and stack
        """
        import Queue
        q = Queue.Queue()
        stack = []
        q.put(node)
        while not q.empty():
            node = q.get()
            stack.append(node)
            if node.right:
                q.put(node.right)
            if node.left:
                q.put(node.left)
        while stack:
            print stack.pop().data,

    def inorderSucessor(self, node):
        """
        Inorder Sucessor of a given node is the next node in the in order traversal
        """
        pass

    def countLeafNodes(self, root):
        """
        count no of leaves nodes in a binary tree
        """
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        else:
            return self.countLeafNodes(root.left) + self.countLeafNodes(root.right)

