#Min elements in shorttest amount of time 
#elements arranged in descending and least val is found 
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self):

        top = self.stack.pop()
        if top == self.minStack[-1]:
            self.minStack.pop()

    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minStack[-1]
    


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())   # Returns -3
minStack.pop()
print(minStack.top())      # Returns 0
print(minStack.getMin())   # Returns -2

