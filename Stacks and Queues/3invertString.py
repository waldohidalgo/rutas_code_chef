class Stack:
    def __init__(self):
        self.MAX_SIZE = 101
        self.a = [''] * self.MAX_SIZE
        self.top = -1

    def push(self, ele):
        if self.top < self.MAX_SIZE - 1:
            self.top += 1
            self.a[self.top] = ele
        

    def pop(self):
        if self.top >= 0:
            ele = self.a[self.top]
            self.top -= 1
            return ele
        

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top >= self.MAX_SIZE

if __name__ == "__main__":
    original_string = "Hello, World!"
    string_length = len(original_string)

    stack = Stack()

    # Push each character onto the stack
    for i in range(string_length):
        c = original_string[i]
        stack.push(c)

    # Pop the characters from the stack to construct the reversed string
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    print(reversed_string)
