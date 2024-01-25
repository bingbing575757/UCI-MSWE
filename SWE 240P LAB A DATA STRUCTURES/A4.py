# from queue import Queue
# # Task-1
# class BSTNode():
#     def __init__(self, student_number, last_name, home_department, program, year):
#         # Initialize the BSTNode object with student data
#         self.student_number = student_number
#         self.last_name = last_name
#         self.home_department = home_department
#         self.program = program
#         self.year = year
#         self.parent = None
#         self.left = None
#         self.right = None
#
#     def data(self):
#         # Return student data as a list
#         return [self.student_number, self.last_name, self.home_department, self.program, self.year]
# class BST():
#     def __init__(self):
#         self.root = None
#
#     def insert(self, target):
#         # Insert a BSTNode into the BST
#         # Must have value of left child <= value of children's parent <= value of right child
#         if self.root is None:
#             self.root = target
#             return
#         parent = None
#         cur = self.root
#         while cur:
#             parent = cur
#             if target.last_name < cur.last_name:
#                 cur = cur.left
#             else:
#                 cur = cur.right
#         if target.last_name < parent.last_name:
#             parent.left = target
#         else:
#             parent.right = target
#
    # def deleteOneNode(self, target):
    #     # Delete a specific node with one child from the BST
    #     if target is None:
    #         return target
    #     if target.right is None:
    #         return target.left
    #     cur = target.right
    #     # Find the leftest child of the cur and put target.left on it.
    #     while cur.left:
    #         cur = cur.left
    #     cur.left = target.left
    #     return target.right
    #
    # def deleteNode(self, Node):
    #     # Delete a node from the BST
    #     if self.root is None:
    #         return self.root
    #     cur = self.root
    #     pre = None  # Records the parent of cur to delete cur
    #     while cur: # To find the node to be deleted
    #         if cur.last_name == Node.last_name:
    #             break
    #         pre = cur
    #         if cur.last_name > Node.last_name:
    #             cur = cur.left
    #         else:
    #             cur = cur.right
    #     if pre is None:  # Only has head
    #         return self.deleteOneNode(cur) # The tree only has None now.
    #     # pre needs to determine whether to delete the left child or the right child
    #     if pre.left and pre.left.last_name == Node.last_name:
    #         pre.left = self.deleteOneNode(cur)
    #     if pre.right and pre.right.last_name == Node.last_name:
    #         pre.right = self.deleteOneNode(cur)
    #     return self.root
#
#
#
#
# # Task-2
#     def in_order_traversal(self, node, result=None):
#         # Node is root here.
#         if result is None:
#             result = []
#         if node is None:
#             return result
#
#         self.in_order_traversal(node.left, result)
#         # recursively traverses the left subtree
#         result.append(node.data())
#         # processes the current node
#         self.in_order_traversal(node.right, result)
#         # recursively traverses the right subtree
#         return result
#
#
#
#
# # Task-3
#
#     def breadth_first_traversal(self):
#         # Output in the order from top to bottom and from left to right.
#         result = []
#         if self.root is None:
#             return result
#         queue = Queue()
#         queue.put(self.root)
#
#         while not queue.empty():
#             node = queue.get()
#             result.append(node.data())
#             if node.left:
#                 queue.put(node.left)
#             if node.right:
#                 queue.put(node.right)
#         return result
#
# def read_student_records(file_path):
#     records = []
#     with open(file_path, mode='rt', encoding='utf-8') as file:
#         for line in file:
#             # Extract operation code, student number, last name, home department, program, and year from each line
#             operation_code = line[0]
#             student_number = line[1:8].strip()
#             last_name = line[8:33].strip()
#             home_department = line[33:37].strip()
#             program = line[37:41].strip()
#             year = line[41:].strip()
#             # Create a new BSTNode object and add it to the records list
#             records.append(BSTNode(student_number, last_name, home_department, program, year))
#     return records
#
# def save_to_file(file_name, result):
#     with open(file_name, mode='w', encoding='utf-8') as output_file:
#         # Iterate through each sublist in the result list
#         for row in result:
#             operation_code = row[0][0]
#             student_number = row[0][1:8]
#             last_name = row[1][:25].ljust(25)
#             home_department = row[2][:4].ljust(4)
#             program = row[3][:4].ljust(4)
#             year = row[4][0]
#
#             # Format the output string, concatenate elements based on the specified format, and add a newline character
#             row_string = f"{operation_code}{student_number}{last_name}{home_department}{program}{year}\n"
#             # Write the string to the file
#             output_file.write(row_string)
#
# # Test code
# if __name__ == "__main__":
#     student_records = read_student_records("tree-input.txt")
#     # The Nodes with value of student data are placed into a list.
#     bst = BST()
#     for record in student_records:
#         bst.insert(record)
#         # print(record.data())
#
#     # Insert operation
#     a = bst.insert(BSTNode("8306700", "Aones", "0251", "CT", "2"))
#     # Test In-Order Traversal
#     result = bst.in_order_traversal(bst.root)
#     save_to_file('output of in-order traversal.txt',result) # You can open the file to check
#     print("In-Order Traversal Result:", result) # Or check the inserted node easily in the run output below
#     # Test delete operation
#     b = bst.deleteNode(BSTNode("8500453", "Banks", "0251", "EST", "1"))
#     # # Test Breadth-First Traversal
#     result2 = bst.breadth_first_traversal()
#     save_to_file('output of breadth-first traversal.txt',result2)
#     print('Breadth-First Traversal Result:', result2)
#
#
from queue import Queue
# Task-1
class BSTNode():
    def __init__(self, student_number, last_name, home_department, program, year, Operation_code = None):
        # Initialize the BSTNode object with student data
        self.student_number = student_number
        self.last_name = last_name
        self.home_department = home_department
        self.program = program
        self.year = year
        self.Operation_code = Operation_code
        self.parent = None
        self.left = None
        self.right = None

    def data(self):
        # Return student data as a list
        return [self.student_number, self.last_name, self.home_department, self.program, self.year]
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
            if target.last_name < cur.last_name:
                cur = cur.left
            else:
                cur = cur.right
        if target.last_name < parent.last_name:
            parent.left = target
        else:
            parent.right = target

    # def deleteNode(self, target_name):
    #     if self.root is None:
    #         return self.root
    #
    #     cur = self.root
    #     pre = None  # Records the parent of cur to delete cur
    #     while cur:  # To find the node to be deleted
    #         if cur.last_name == target_name:
    #             break
    #         pre = cur
    #         if cur.last_name > target_name:
    #             cur = cur.left
    #         else:
    #             cur = cur.right
    #
    #     if cur is None:  # Node with target_name not found
    #         return self.root
    #
    #     if cur.left and cur.right:
    #         # Node to be deleted has two children
    #         successor_parent = cur
    #         successor = cur.right
    #         while successor.left:
    #             successor_parent = successor
    #             successor = successor.left
    #
    #         # Replace cur's data with successor's data
    #         cur.student_number = successor.student_number
    #         cur.last_name = successor.last_name
    #         cur.home_department = successor.home_department
    #         cur.program = successor.program
    #         cur.year = successor.year
    #
    #         # Delete the successor node
    #         if successor_parent.left == successor:
    #             successor_parent.left = self.deleteOneNode(successor)
    #         else:
    #             successor_parent.right = self.deleteOneNode(successor)
    #
    #     else:
    #         # Node to be deleted has at most one child
    #         child = cur.left if cur.left else cur.right
    #         if pre is None:
    #             # Node to be deleted is the root
    #             self.root = child
    #         elif pre.left == cur:
    #             pre.left = child
    #         else:
    #             pre.right = child
    #
    #     return self.root
    # def deleteOneNode(self, target):
    #     # Delete a specific node with one child from the BST
    #     if target is None:
    #         return target
    #     if target.right is None:
    #         return target.left
    #     cur = target.right
    #     # Find the leftest child of the cur and put target.left on it.
    #     while cur.left:
    #         cur = cur.left
    #     cur.left = target.left
    #     return target.right
    #
    # def deleteNode(self, target_name):
    #     # Delete a node from the BST
    #     if self.root is None:
    #         return self.root
    #     cur = self.root
    #     pre = None  # Records the parent of cur to delete cur
    #     while cur: # To find the node to be deleted
    #         if cur.last_name == target_name:
    #             break
    #         pre = cur
    #         if cur.last_name > target_name:
    #             cur = cur.left
    #         else:
    #             cur = cur.right
    #     if pre is None:  # Only has head
    #         return self.deleteOneNode(cur) # The tree only has None now.
    #     # pre needs to determine whether to delete the left child or the right child
    #     if pre.left and pre.left.last_name == target_name:
    #         pre.left = self.deleteOneNode(cur)
    #     if pre.right and pre.right.last_name == target_name:
    #         pre.right = self.deleteOneNode(cur)
    #     return self.root
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
    def deleteNode(self, target):
        if self.root is None:
            return
        cur = self.root
        pre = None
        while cur:
            if cur.last_name == target.last_name:
                break
            pre = cur
            if cur.last_name > target.last_name:
                cur = cur.left
            elif cur.last_name < target.last_name:
                cur = cur.right
        if pre is None and cur.last_name == target.last_name:
            return self.deleteOneNode(cur)
        if pre.left and pre.left.last_name == target.last_name:
            pre.left = self.deleteOneNode(cur)
            return
        if pre.right and pre.right.last_name == target.last_name:
            pre.right = self.deleteOneNode(cur)
            return
        print('Fail to Delete')
        return




# Task-2
    def in_order_traversal(self, node, result=None):
        # Node is root here.
        if result is None:
            result = []
        if node is None:
            return result

        self.in_order_traversal(node.left, result)
        # recursively traverses the left subtree
        result.append(node.data())
        # processes the current node
        self.in_order_traversal(node.right, result)
        # recursively traverses the right subtree
        return result




# Task-3

    def breadth_first_traversal(self):
        # Output in the order from top to bottom and from left to right.
        result = []
        if self.root is None:
            return result
        queue = Queue()
        queue.put(self.root)

        while not queue.empty():
            node = queue.get()
            result.append(node.data())
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
        return result

def read_student_records(file_path):
    records = []
    with open(file_path, mode='rt', encoding='utf-8') as file:
        for line in file:
            # Extract operation code, student number, last name, home department, program, and year from each line
            operation_code = line[0]
            student_number = line[1:8].strip()
            last_name = line[8:33].strip()
            home_department = line[33:37].strip()
            program = line[37:41].strip()
            year = line[41:].strip()
            # Create a new BSTNode object and add it to the records list
            records.append(BSTNode(student_number, last_name, home_department, program, year, operation_code))
    return records

def save_to_file(file_name, result):
    with open(file_name, mode='w', encoding='utf-8') as output_file:
        # Iterate through each sublist in the result list
        for row in result:
            operation_code = row[0][0]
            student_number = row[0][1:8]
            last_name = row[1][:25].ljust(25)
            home_department = row[2][:4].ljust(4)
            program = row[3][:4].ljust(4)
            year = row[4][0]

            # Format the output string, concatenate elements based on the specified format, and add a newline character
            row_string = f"{operation_code}{student_number}{last_name}{home_department}{program}{year}\n"
            # Write the string to the file
            output_file.write(row_string)

# Test code
# if __name__ == "__main__":
#     student_records = read_student_records("tree-input.txt")
#     # The Nodes with value of student data are placed into a list.
#     bst = BST()
#     for record in student_records:
#         bst.insert(record)
#         # print(record.data())
#
#     # Insert operation
#     a = bst.insert(BSTNode("8306700", "Aones", "0251", "CT", "2","I"))
#     # Test In-Order Traversal
#     # result = bst.in_order_traversal(bst.root)
#     # save_to_file('output of in-order traversal.txt',result) # You can open the file to check
#     # print("In-Order Traversal Result:", result) # Or check the inserted node easily in the run output below
#     # # Test delete operation
#     b = bst.deleteNode(BSTNode("8301164", "Bannister", "0251", "EST", "1"))
#     # # Test Breadth-First Traversal
#     result20 = bst.in_order_traversal(bst.root)
#     print("In-Order Traversal Result:", result20)
#     # result2 = bst.breadth_first_traversal()
#     save_to_file('output of in-order traversal.txt',result20)
#     # print('Breadth-First Traversal Result:', result2)


if __name__ == "__main__":
    student_records = read_student_records("tree-input.txt")
    # The Nodes with value of student data are placed into a list.
    bst = BST()
    for record in student_records:
        bst.insert(record)
    # # Test delete operation1: Nonexistence
    # b = bst.deleteNode(BSTNode("8301164", "BBB", "0251", "EST", "1"))
    # result10 = bst.in_order_traversal(bst.root)
    # print("In-Order Traversal Result:", result10)
    # save_to_file('output of in-order traversal.txt',result10)
    # Test delete operation2: Existence
    c = bst.deleteNode(BSTNode("8301164", "Bannister", "0251", "EST", "1"))
    result20 = bst.in_order_traversal(bst.root)
    print("In-Order Traversal Result:", result20)
    save_to_file('output of in-order traversal.txt',result20)


