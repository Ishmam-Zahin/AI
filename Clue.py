from Logic  import *

def main():
    mustard = Symbol("i am mustard")
    plum = Symbol("i am plum")
    scarlet = Symbol("i am scarlet")
    characters = [mustard, plum, scarlet]

    ballroom = Symbol("ballroom")
    kitchen = Symbol("kitchen")
    library = Symbol("library")
    rooms = [ballroom, kitchen, library]

    knife = Symbol("used knife")
    revolver = Symbol("used revolver")
    wrench = Symbol("used wrench")
    weapons = [knife, revolver, wrench]

    symbols = characters + rooms + weapons

    knowledge = And(
        Or(mustard, plum, scarlet),
        Or(ballroom, kitchen, library),
        Or(knife, revolver, wrench),
        Not(mustard),
        Not(kitchen),
        Not(revolver),
        Or(
            Not(scarlet),
            Not(library),
            Not(wrench)
        ),
        Not(plum),
        Not(ballroom)
    )


    for symbol in symbols:
        x = modelCheck(knowledge, symbol, symbols)
        if x == -1:
            print(f"{symbol.name} => FALSE")
        elif x == 0:
            print(f"{symbol.name} => MAYBE")
        else:
            print(f"{symbol.name} => TRUE")





if __name__ == "__main__":
    main()