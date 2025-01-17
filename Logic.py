class Symbol:
    symbolsList = []
    def __init__(self, sentence):
        self.name = sentence
        self.value = True
        Symbol.symbolsList.append(self)
    
    def evaluate(self):
        return


class Not(Symbol):
    def __init__(self, symbol):
        self.symbol = symbol
        self.evaluate()
    
    def evaluate(self):
        self.symbol.evaluate()
        if self.symbol.value:
            self.value = False
        else:
            self.value = True



class And(Symbol):
    def __init__(self, *symbols):
        self.symbols = symbols
        self.evaluate()
    
    def evaluate(self):
        tmpValue = True
        for symbol in self.symbols:
            symbol.evaluate()
            tmpValue = tmpValue and symbol.value
        
        self.value = tmpValue
    
    def add(self, symbol):
        self.symbols = self.symbols + (symbol, )
        self.evaluate()


class Or(Symbol):
    def __init__(self, *symbols):
        self.symbols = symbols
        self.evaluate()
    
    def evaluate(self):
        tmpValue = False
        for symbol in self.symbols:
            symbol.evaluate()
            tmpValue = tmpValue or symbol.value
        
        self.value = tmpValue

class Implication(Symbol):
    def __init__(self, leftSymbol, rightSymbol):
        self.symbols = (leftSymbol, rightSymbol)
        self.evaluate()
    
    def evaluate(self):
        for i, symbol in enumerate(self.symbols):
            symbol.evaluate()
            if i == 0:
                l = symbol
            else:
                r = symbol
        
        if l.value and (not r.value):
            self.value = False
        else:
            self.value = True



def modelCheck(kb, target, symbols):
    length = len(symbols)
    x = 2 ** length
    kbCount = 0
    targetCount = 0
    for num in range(x):
        for i in range(length):
            v = bool(num & 1)
            num = num >> 1
            symbols[i].value = v
        
        kb.evaluate()
        if kb.value:
            for symbol in Symbol.symbolsList:
                print(symbol.value, end=" ")
            print()

        if kb.value:
            kbCount += 1
            if target.value:
                targetCount += 1
            else:
                targetCount -= 1
        
    if (kbCount == targetCount) and kbCount > 0:
        return 1
    elif (kbCount + targetCount == 0):
        return -1
    else:
        return 0






def main():
    obj1 = Symbol("ishmam")
    obj2 = Symbol("ishmam")

    print(obj1, obj2)
    print(Symbol.symbolsList)


if __name__ == "__main__":
    main()