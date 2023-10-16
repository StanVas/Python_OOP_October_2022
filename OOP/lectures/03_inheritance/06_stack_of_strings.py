# A mixin is a class that provides method implementations for reuse by multiple related child classes.
class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


ss = Stack()
ss.push('1')
ss.push('2')
ss.push('3')
print(ss)

