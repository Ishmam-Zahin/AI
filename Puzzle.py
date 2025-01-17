from Logic import *

def main():
    persons = ["Gilderoy", "Pomona", "Minerva", "Horace"]
    houses = ["Gryfindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    symbols = []
    mp = {}
    knowledge = And()

    for person in persons:
        for house in houses:
            tmp = Symbol(f"{person}{house}")
            symbols.append(tmp)
            mp[f"{person}{house}"] = tmp
    
    knowledge.add(Or(*symbols))
    

    for person in persons:
        for h1 in houses:
            for h2 in houses:
                if h1 != h2:
                    tmp1 = f"{person}{h1}"
                    tmp2 = f"{person}{h2}"
                    x = Implication(mp[tmp1], Not(mp[tmp2]))
                    knowledge.add(x)
    
    for house in houses:
        for p1 in persons:
            for p2 in persons:
                if p1 != p2:
                    tmp1 = f"{p1}{house}"
                    tmp2 = f"{p2}{house}"
                    x = Implication(mp[tmp1], Not(mp[tmp2]))
                    knowledge.add(x)
    

    knowledge.add(Or(mp[persons[0] + houses[0]], mp[persons[0] + houses[2]]))
    knowledge.add(Not(mp[persons[1] + houses[3]]))
    knowledge.add(mp[persons[2] + houses[0]])
    # knowledge.add(mp[persons[1] + houses[1]])

    print(modelCheck(knowledge, mp["PomonaHufflepuff"], symbols))
    

    # for symbol in symbols:
    #     x = modelCheck(knowledge, symbol, symbols)
    #     if x == -1:
    #         print(f"{symbol.name} ==>> ❌❌❌")
    #     elif x == 0:
    #         print(f"{symbol.name} ==>> ⭕⭕⭕")
    #     else:
    #         print(f"{symbol.name} ==>> ✔️✔️✔️")


    # for symbol in Symbol.symbolsList:
    #     print(symbol.name)

    modelCheck(knowledge, mp[persons[1]+houses[1]], symbols)







if __name__ == "__main__":
    main()