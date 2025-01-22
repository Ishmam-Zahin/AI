class Node:
    def __init__(self, *, value = None, parentFront = None, parentBack = None):
        self.value = value
        self.parentFront = parentFront
        self.parentBack = parentBack

class List:
    def __init__(self):
        self.root = None
        self.lastNode = self.root
        self.length = 0

    def add(self, value):
        if self.root == None:
            self.root = Node(value = value)
            self.lastNode = self.root
        else:
            newNode = Node(value = value)
            newNode.parentBack = self.lastNode
            self.lastNode.parentFront = newNode
            self.lastNode = newNode
        
        self.length += 1