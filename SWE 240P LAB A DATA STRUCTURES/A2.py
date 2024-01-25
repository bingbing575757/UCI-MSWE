import re
# Task-1
class LinkedStack:
    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    class Empty(Exception):
        """Error attempting to access an element from an empty container."""
        pass

    def __init__(self):
        self._head = None
        self._size = 0

    def size(self):
        # returns the size of the stack
        return self._size

    def push(self, e):
        # pushes element which is the top element in the linkedlist in the stack
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        # removes the latest element which is the top element in the linkedlist from the stack and returns it
        if self._head is None:
            raise self.Empty('Stack is empty')
        # Raise Empty exception if the stack is empty.
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def peek(self):
        # returns the latest element from the stack without removing it
        if self._head is None:
            raise self.Empty('Stack is empty')
        # Raise Empty exception if the stack is empty.
        answer = self._head._element
        return answer

    def reverse_stack(self):
        # Reverse the stack / Be used for task2
        temp_stack = LinkedStack()
        while self.size() > 0:
            temp_stack.push(self.pop())
        return temp_stack

if __name__ == "__main__":
    print('Test for task1')
    stack = LinkedStack()

    # tests push and size methods
    stack.push(1)   # [1]
    print('After push 1, stack size is',stack.size())
    stack.push(2)   # [2, 1]
    print('After push 2, stack size is',stack.size())

    # tests peek method
    print('stack.peek() is',stack.peek())

    # tests pop method
    print('stack.pop()',stack.pop())
    print('After pop, stack size', stack.size())
    print('stack.pop()',stack.pop())
    print('After pop again, stack size', stack.size())

    # tests the pop method on an empty stack
    try:
        stack.pop()
    except stack.Empty:
        print("Empty exception is raised for pop operation on an empty stack.")

    # tests the peek method on an empty stack
    try:
        stack.peek()
    except stack.Empty:
        print("Empty exception is raised for peek operation on an empty stack.")

    print("All test cases passed successfully.")




# Task-2
class ArithmeticExpressionEvaluator:
    def tokenize_expression(self,expression):
        tokens = re.findall(r'\d+|\S', expression)
        return tokens
    def evaluate_expression(self,expression):
        tokens = self.tokenize_expression(expression)
        stack = LinkedStack()
        operators = set(['+', '-', '*', '/'])

        for token in tokens:
            if stack.size() > 0 and token.isdigit() and stack.peek() in ['*', '/']:
                operand2 = token
                operator = stack.pop()
                operand1 = stack.pop()
                if operator == '*':
                    stack.push(int(operand1) * int(operand2))
                elif operator == '/':
                    if operand2 == 0:
                        return 'NAN'
                    stack.push(int(operand1) / int(operand2))
            elif token not in operators and token.isdigit() is False:
                return 'NaN'
            else:
                stack.push(token)
        if stack.size() == 1:
            return stack.pop()
        stack1 = stack.reverse_stack()

        while stack1.size() > 1:
               operand1 = stack1.pop()
               operator = stack1.pop()
               operand2 = stack1.pop()
               if operator == '+':
                   stack1.push(int(operand1) + int(operand2))
               elif operator == '-':
                   stack1.push(int(operand1) - int(operand2))
        return stack1.pop()

if __name__ == "__main__":
    print('Test for task2')
    evaluator = ArithmeticExpressionEvaluator()

    expression1 = "10 + 20 * 2 - 8 /      2   * 2  "
    result1 = evaluator.evaluate_expression(expression1)
    print(f"Expression: {expression1} => Result: {result1}")


    expression2 = "foo / 30 + 7"
    result2 = evaluator.evaluate_expression(expression2)
    print(f"Expression: {expression2} => Result: {result2}")




# Task-3
class Queue:
    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def size(self):
        # returns the size of the queue
        return self._size

    def is_empty(self):
        return self._size == 0

    def poll(self):
        # returns the earliest element without removing it
        if self.is_empty():
            return None
        return self._head._element

    def enqueue(self, e):
        # enqueue element in the queue
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            cur = self._head
            while cur._next is not None:
                cur = cur._next
            cur._next = newest

        self._size += 1

    def dequeue(self):
        # removes and returns the earliest element from the queue
        if self.is_empty():
            return None
        head = self._head
        answer = head._element
        self._head = self._head._next
        self._size -= 1
        return answer


if __name__ == "__main__":
    print('Test for task3')
    q = Queue()
    print("Is queue empty?", q.is_empty())

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print("Is queue empty?", q.is_empty())
    print("Queue size:", q.size())      # Output: 3

    print("First element in the queue:", q.poll())  # Output: 1

    item = q.dequeue()
    print("Removed element:", item)  # Output: 1
    print("Queue size after dequeue:", q.size())  # Output: 2




# # Task-4
class StackWithTwoQs:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue() # final

    def push(self, x):
        # pushes x in the stack
        self.queue1.enqueue(x)
        # Move all elements from queueTwo to queueOne
        while not self.queue2.is_empty():
            self.queue1.enqueue(self.queue2.dequeue())

        self.queue1, self.queue2 = self.queue2, self.queue1
        print('此时',self.queue2.poll())

    def pop(self):
        # removes the latest element from the stack and returns it
        if self.queue2.is_empty():
            return None
        return self.queue2.dequeue()

    def peek(self):
        # returns the latest element from the stack without removing it
        if self.queue2.is_empty():
            return None
        return self.queue2.poll()

    def size(self):
        # returns the size of the stack
        return self.queue2.size()

if __name__ == "__main__":
    print('Test for task4')
    stack = StackWithTwoQs()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("pop:",stack.pop())
    print('peek:',stack.peek())
    print('size:',stack.size())






