def func1():
    x = 10
    def func2():
        x = 15
        def func3():
            nonlocal x
            x = 20
        func3()
    func2()
    print(x)

def main():
    func1()



if __name__ == "__main__":
    main()