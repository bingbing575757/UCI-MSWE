from queue import Queue
# Task-1:
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class HeapBuilder:
# Except for the last level, all other levels are filled, and the nodes in the last level are left-aligned.
# Assume placing elements from the list into the binary tree from top to bottom and from left to right initially.
    def __init__(self, my_list):
        self.my_list0 = [0] + my_list[ : ]
        # Setting [0] is for the convenience of calculating the indices of the nodes' left and right children.
        self.size = len(my_list)

# Min HeapBuilder
    def percDown_min(self,i):
        # Perform a percolation operation on the node at the specified position i, continuing until the minimum heap property is satisfied
        while(i*2) <= self.size:
            mc = self.minChild(i)
            if self.my_list0[i] > self.my_list0[mc]:
                tmp = self.my_list0[i]
                self.my_list0[i] = self.my_list0[mc]
                self.my_list0[mc] = tmp
            i = mc

    def minChild(self, i):
        # Find the index of the smaller child node for the node at the specified position i.
        if i * 2 + 1 > self.size:
            return i*2
        else:
            if self.my_list0[i * 2] < self.my_list0[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def build_min_heap(self):
        i = self.size // 2
        while (i > 0):
            self.percDown_min(i)
            i = i - 1
        return self.my_list0

    def level_order_traversal(self, root):
        result = []
        if not root:
            return result

        queue = Queue()
        queue.put(root)

        while not queue.empty():
            level_nodes = []
            level_size = queue.qsize()
            for _ in range(level_size):
                node = queue.get()
                level_nodes.append(node.data)
                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)
            result.append(level_nodes)

        return result

    def createMinHeapTree(self):
        min_heap = self.build_min_heap()[1:]
        print(min_heap)
        root = Node(min_heap[0])
        queue = [root]
        i = 0
        while i < len(min_heap):
            current = queue.pop(0)
            left_child_index = 2 * i + 1
            right_child_index = 2 * i + 2
            i += 1
            if left_child_index < len(min_heap):
                current.left = Node(min_heap[left_child_index])
                queue.append(current.left)
            if right_child_index < len(min_heap):
                current.right = Node(min_heap[right_child_index])
                queue.append(current.right)

        # 调用广度优先搜索函数，获取按行遍历的结果
        return self.level_order_traversal(root)

# Max HeapBuilder
    def percDown_max(self, i):
        while i * 2 <= self.size:
            mc = self.maxChild(i)
            if self.my_list0[i] < self.my_list0[mc]: # change '>' to '<' compared with min case
                tmp = self.my_list0[i]
                self.my_list0[i] = self.my_list0[mc]
                self.my_list0[mc] = tmp
            i = mc

    def maxChild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.my_list0[i * 2] > self.my_list0[i * 2 + 1]: # change '<' to '>' compared with min case
                return i * 2
            else:
                return i * 2 + 1

    def build_max_heap(self):
    # It is similar to the min case
        i = self.size // 2
        while i > 0:
            self.percDown_max(i)
            i -= 1
        return self.my_list0

    def createMaxHeapTree(self):
    # Just changes 'min' to 'max' compared to min case.
        max_heap = self.build_max_heap()[1:]
        root = Node(max_heap[0])
        queue = [root]
        i = 0
        while i < len(max_heap):
            current = queue.pop(0)
            left_child_index = 2 * i + 1
            right_child_index = 2 * i + 2
            i += 1
            if left_child_index < len(max_heap):
                current.left = Node(max_heap[left_child_index])
                queue.append(current.left)
            if right_child_index < len(max_heap):
                current.right = Node(max_heap[right_child_index])
                queue.append(current.right)
        return self.level_order_traversal(root)

if __name__ == "__main__":
    # Sample test cases
    min_heap_values = HeapBuilder([3, 2, 1, 4, 5])
    # Test Min Heap
    min_heap_tree = min_heap_values.createMinHeapTree()
    print(min_heap_tree)
    # Test Max Heap
    max_heap_values = HeapBuilder([3, 2, 1, 4, 5])
    max_heap_tree = max_heap_values.createMaxHeapTree()
    print(max_heap_tree)




# Task-2:

from A51 import BSTNode, BST
class BSTToHeapTransformer(BST,HeapBuilder):
    @staticmethod
    def bstToMinHeap(bst_list):
        return HeapBuilder.createMinHeapTree(bst_list)

    @staticmethod
    def bstToMaxHeap(bst_list):
        return HeapBuilder.createMaxHeapTree(bst_list)

if __name__ == "__main__":
    a = [3,2,1,4,5]
    bst = BST()
    for value in a:
        bst.insert(BSTNode(value))
    # We have the root node of a BST now
    print(bst.root)
    result = bst.in_order_traversal(bst.root)

    heap_values = HeapBuilder(result)
    # Test the bstToMinHeap method
    result1 = BSTToHeapTransformer.bstToMinHeap(heap_values)
    print(result1)
    # Test the bstToMaxHeap method
    result2 = BSTToHeapTransformer.bstToMaxHeap(heap_values)
    print(result2)











