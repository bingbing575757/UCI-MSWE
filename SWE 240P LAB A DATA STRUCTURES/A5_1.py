from queue import Queue

# General version of BST
class BSTNode():
    def __init__(self,value):
        # Initialize the BSTNode object with student data
        self.value = value
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None

    def insert(self, target):
        # Insert a BSTNode into the BST
        # Must have value of left child <= value of children's parent <= value of right child
        if self.root is None:
            self.root = target
            return
        parent = None
        cur = self.root
        while cur:
            parent = cur
            if target.value < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        if target.value < parent.value:
            parent.left = target
        else:
            parent.right = target

    def deleteOneNode(self, target):
        # Delete a specific node with one child from the BST
        if target is None:
            return target
        if target.right is None:
            return target.left
        cur = target.right
        # Find the leftest child of the cur and put target.left on it.
        while cur.left:
            cur = cur.left
        cur.left = target.left
        return target.right

    def deleteNode(self, Node):
        # Delete a node from the BST
        if self.root is None:
            return self.root
        cur = self.root
        pre = None  # Records the parent of cur to delete cur
        while cur: # To find the node to be deleted
            if cur.value == Node.value:
                break
            pre = cur
            if cur.value > Node.valuee:
                cur = cur.left
            else:
                cur = cur.right
        if pre is None:  # Only has head
            return self.deleteOneNode(cur) # The tree only has None now.
        # pre needs to determine whether to delete the left child or the right child
        if pre.left and pre.left.value == Node.value:
            pre.left = self.deleteOneNode(cur)
        if pre.right and pre.right.value == Node.value:
            pre.right = self.deleteOneNode(cur)
        return self.root

    def in_order_traversal(self, node, result=None):
        # Node is root here.
        if result is None:
            result = []
        if node is None:
            return result

        self.in_order_traversal(node.left, result)
        # recursively traverses the left subtree
        result.append(node.value)
        # processes the current node
        self.in_order_traversal(node.right, result)
        # recursively traverses the right subtree
        return result

    def breadth_first_traversal(self):
        # Output in the order from top to bottom and from left to right.
        result = []
        if self.root is None:
            return result
        queue = Queue()
        queue.put(self.root)

        while not queue.empty():
            node = queue.get()
            result.append(node.value)
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
        return result

