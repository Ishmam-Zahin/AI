from List import List

class Queue(List):
    def __init__(self):
        super().__init__()
    
    def push(self, value):
        super().add(value)
    
    def pop(self):
        if self.root == None:
            return
        elif self.root == self.lastNode and self.root != None:
            self.root = None
            self.lastNode = self.root
        else:
            self.root = self.root.parentFront
            self.root.parentBack = None
        
        self.length -= 1
    
    def front(self):
        if self.root != None:
            return self.root.value
        else:
            return None




def main():
    obj = Queue()
    obj.push(4)
    obj.push(47)
    obj.push(34)
    obj.push(44)
    obj.push(40)

    while obj.front():
        print(obj.front(), obj.length)
        obj.pop()


if __name__ == "__main__":
    main()