class MyQueue(object):

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.move()
        return self.stack_out.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.stack_out[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack_in and not self.stack_out

    def move(self):
        """
        Move elements from stack_in to stack_out if stack_out is empty.
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

# Ejemplo de uso:
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.pop())    # Debería devolver 1
print(obj.peek())   # Debería devolver 2
print(obj.empty())  # Debería devolver False
