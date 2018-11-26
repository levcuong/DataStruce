class Stack:
    def __init__(self):
        self.stack = []
    
    def add(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False
    
    def remove(self):
        if(len(self.stack) <= 0):
            return("No element in the Stack")
        else:
            return self.stack.pop()
    def peek(self):
        return self.stack[0]

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
print(AStack.remove())
AStack.add("Wed")
AStack.add("Thu")
print(AStack.remove())