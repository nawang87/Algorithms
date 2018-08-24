class stackofplates:
    def __init__(self,threshold):
        self.t= threshold
        self.stack = [[]]

    def push(self,x):
        if len(self.stack[-1])==self.t:
            newstack = [x]
            self.stack.append(newstack)
        else:
            self.stack[-1].append(x)


    def pop(self):
        # print(self.stack)
        if len(self.stack)>0:
            popped = self.stack[-1][-1]
            del self.stack[-1][-1]
            if len(self.stack[-1]) == 0:
                del self.stack[-1]
            print("Pop", self.stack)
            return popped
        return None

    def popAt(self, index):
        popped = self.stack[index][-1]
        del self.stack[index][-1]
        if len(self.stack[index]) == 0:
            del self.stack[index]
        print("PopAt",self.stack)
        return popped



s = stackofplates(5)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.pop()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.popAt(0)

