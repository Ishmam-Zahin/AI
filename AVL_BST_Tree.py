class Node:
    def __init__(self, value, parent = None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.height = 1

class AVL_BST_Tree:
    def __init__(self, allowDuplicates = False):
        self.root = None
        self.allowDuplicates = allowDuplicates
    
    def find(self, value):
        node = self.root

        while node != None:
            if value == node.value:
                break
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        
        return node
    
    def getBalanceFactor(self, node, l = 0, r = 0):
        if node.left != None:
            l = node.left.height
        if node.right != None:
            r = node.right.height

        return (l - r)
    
    def fixHeight(self, node):
        l= 0
        r=0
        if node.right != None:
            r = node.right.height
        if node.left != None:
            l = node.left.height
        node.height = 1 + max(r, l)
    
    def RR_Rotate(self, x, y, z, parent):
        tmp = y.left
        y.left = x
        x.parent = y
        y.right = z
        z.parent = y
        x.right = tmp
        if tmp != None:
            tmp.parent = x
        y.parent = parent

        if parent != None:
            if parent.left == x:
                parent.left = y
            else:
                parent.right = y
        else:
            self.root = y
        
        self.fixHeight(x)
        self.fixHeight(z)
        self.fixHeight(y)
        if parent != None:
            self.fixHeight(parent)
    
    def RL_Rotate(self, x, y, z, parent):
        tmp1 = z.left
        tmp2 = z.right
        z.left = x
        z.right = y
        x.parent = z
        y.parent = z
        x.right = tmp1
        if tmp1 != None:
            tmp1.parent = x
        y.left = tmp2
        if tmp2 != None:
            tmp2.parent = y
        z.parent = parent

        if parent != None:
            if parent.left == x:
                parent.left = z
            else:
                parent.right = z
        else:
            self.root = z
        
        self.fixHeight(y)
        self.fixHeight(x)
        self.fixHeight(z)
        if parent != None:
            self.fixHeight(parent)
    
    def LR_Rotate(self, x, y, z, parent):
        tmp1 = z.left
        tmp2 = z.right
        z.left = y
        z.right = x
        y.parent = z
        x.parent = z
        y.right = tmp1
        if tmp1 != None:
            tmp1.parent = y
        x.left = tmp2
        if tmp2 != None:
            tmp2.parent = x
        z.parent = parent

        if parent != None:
            if parent.left == x:
                parent.left = z
            else:
                parent.right = z
        else:
            self.root = z
        
        self.fixHeight(y)
        self.fixHeight(x)
        self.fixHeight(z)
        if parent != None:
            self.fixHeight(parent)
    
    def LL_Rotate(self, x, y, z, parent):
        tmp = y.right
        y.left = z
        z.parent = y
        y.right = x
        x.parent = y
        x.left = tmp
        if tmp != None:
            tmp.parent = x
        y.parent = parent

        if parent != None:
            if parent.left == x:
                parent.left = y
            else:
                parent.right = y
        else:
            self.root = y

        self.fixHeight(x)
        self.fixHeight(z)
        self.fixHeight(y)
        if parent != None:
            self.fixHeight(parent)
    
    def fixBalance(self, node, value = None):
        parent = node.parent
        bType = ""
        x = node

        if value != None:
            if value < x.value:
                y = x.left
                bType += "L"
            else:
                y = x.right
                bType += "R"
            
            if value < y.value:
                z = y.left
                bType += "L"
            else:
                z = y.right
                bType += "R"
        else:
            l = 0
            r = 0
            if x.left != None:
                l = x.left.height
            if x.right != None:
                r = x.right.height
            if l >= r:
                y = x.left
                bType += "L"
            else:
                y = x.right
                bType += "R"
            
            l = 0
            r = 0
            if y.left != None:
                l = y.left.height
            if y.right != None:
                r = y.right.height
            if l >= r:
                z = y.left
                bType += "L"
            else:
                z = y.right
                bType += "R"
        
        
        if bType == "LL":
            self.LL_Rotate(x, y, z, parent)
        elif bType == "LR":
            self.LR_Rotate(x, y, z, parent)
        elif bType == "RL":
            self.RL_Rotate(x, y, z, parent)
        elif bType == "RR":
            self.RR_Rotate(x, y, z, parent)

    def checkBalanceFactors(self, node, value = None):
        while node != None:
                self.fixHeight(node)
                
                balanceFactor = self.getBalanceFactor(node)
                if balanceFactor < -1 or balanceFactor > 1:
                    self.fixBalance(node, value)
                
                node = node.parent

    def add(self, value):
        if self.root == None:
            self.root = Node(value)
            return True
        
        parent = self.root
        while True:
            if value < parent.value:
                if parent.left == None:
                    parent.left = Node(value, parent = parent)
                    break
                else:
                    parent = parent.left
                    continue
            elif value > parent.value:
                if parent.right == None:
                    parent.right = Node(value, parent = parent)
                    break
                else:
                    parent = parent.right
                    continue
            else:
                if self.allowDuplicates == True:
                    if parent.right == None:
                        parent.right = Node(value, parent = parent)
                        break
                    else:
                        parent = parent.right
                        continue
                else:
                    parent = None
                    break
        
        if parent == None:
            return False
        else:
            self.checkBalanceFactors(parent, value = value)
            return True
    
    def traverse(self, node = None, initialCall = True):
        if initialCall:
            node = self.root

        if node == None:
            return
        
        stack = []
        stack.append(node)
        while len(stack) > 0:
            tmp = []
            for n in stack:
                if n != None:
                    print(n.value, end=" ")
                    tmp.append(n.left)
                    tmp.append(n.right)
                else:
                    print("None", end=" ")
            print()
            stack.clear()
            stack = tmp

    def findMinNode(self, node):
        if node.left == None:
            return node
        else:
            return self.findMinNode(node.left)
    
    def findMaxNode(self, node):
        if node.right == None:
            return node
        else:
            return self.findMaxNode(node.right)

    def remove(self, *, node = None, value = None):
        if node == None:
            node = self.root
        
        if node.value == value or value == None:
            parent = node.parent
            if node.left == None and node.right == None:
                if parent == None:
                    self.root = None
                elif parent.left == node:
                    parent.left = None
                elif parent.right == node:
                    parent.right = None
                else:
                    raise Exception("0Failed to delete the node")
                
                self.checkBalanceFactors(parent, value = None)
                return True
            elif node.right == None:
                if parent == None:
                    self.root = node.left
                    node.left.parent = None
                elif parent.left == node:
                    parent.left = node.left
                    node.left.parent = parent
                elif parent.right == node:
                    parent.right = node.left
                    node.left.parent = parent
                else:
                    raise Exception("1Failed to delete the node")
                
                self.checkBalanceFactors(parent, value = None)
                return True
            elif node.left == None:
                if parent == None:
                    self.root = node.right
                    node.right.parent = None
                elif parent.left == node:
                    parent.left = node.right
                    node.right.parent = parent
                elif parent.right == node:
                    parent.right = node.right
                    node.right.parent = parent
                else:
                    raise Exception("2Failed to delete the node")
                
                self.checkBalanceFactors(parent, value = None)
                return True
            else:
                minNode = self.findMinNode(node.right)
                node.value = minNode.value
                return self.remove(node = node.right, value = minNode.value)
        elif value < node.value and node.left != None:
            return self.remove(node = node.left, value = value)
        elif node.right != None:
            return self.remove(node = node.right, value = value)
        else:
            return False



def main():
    obj = AVL_BST_Tree(allowDuplicates=False)
    obj.add(6)
    obj.add(25)
    obj.add(30)
    obj.add(50)
    obj.add(52)
    obj.add(60)
    obj.add(70)
    obj.add(75)

    obj.traverse()
    obj.remove(value=52)
    obj.traverse()



if __name__ == "__main__":
    main()