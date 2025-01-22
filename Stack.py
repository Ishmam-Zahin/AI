from List import List

class Stack(List):
    def __int__(self):
        super().__init__()
    
    def push(self, value):
        super().add(value)

    def pop(self):
        if self.lastNode == None:
            return
        elif self.lastNode == self.root and self.root != None:
            self.root = None
            self.lastNode = self.root
        else:
            self.lastNode = self.lastNode.parentBack
            self.lastNode.parentFront = None
        
        self.length -= 1
    
    def top(self):
        if self.lastNode != None:
            return self.lastNode.value
        else:
            return None



def main():
    obj = Stack()
    obj.push(4)
    obj.push(47)
    obj.push(34)
    obj.push(44)
    obj.push(40)

    while obj.top():
        print(obj.top(), obj.length)
        obj.pop()


if __name__ == "__main__":
    main()