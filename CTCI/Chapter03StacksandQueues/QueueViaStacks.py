class queueviastacks:
    def __init__(self):
        self.pushstack =[]
        self.popstack =[]

    def enqueue(self,x):
        self.pushstack.append(x)

    def dequeue(self):
        if len(self.popstack) > 0:
            return self.popstack.pop()
        else:
            if len(self.pushstack)>0:
                for i in range(len(self.pushstack)):
                    self.popstack.append(self.pushstack.pop())
                return self.popstack.pop()
            else:
                return None

    def peek(self):
        if len(self.popstack) > 0:
            return self.popstack[-1]
        else:
            if len(self.pushstack) > 0:
                for i in range(len(self.pushstack)):
                    self.popstack.append(self.pushstack.pop())
                return self.popstack[-1]
            else:
                return None

    def empty(self):
        return len(self.pushstack) + len(self.popstack) == 0
