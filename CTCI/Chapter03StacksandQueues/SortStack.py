class sortStack:
    def __init__(self):
        self.stack = []
        self.auxstack =[]

    def push(self,x):
        while self.peek() is not None and x>self.peek():
            self.auxstack.append(self.stack.pop())
        self.stack.append(x)
        while len(self.auxstack)>0:
            self.stack.append(self.auxstack.pop())

    def pop(self):
        self.stack.pop()

    def peek(self):
        if len(self.stack)>0:
            return self.stack[-1]
        return None


s = sortStack()
s.push(1)
s.push(2)
s.push(4)
s.push(0)
s.push(5)
s.pop()
s.push(3)


