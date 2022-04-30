def f1():
    x = 10
    def f2 ():
        nonlocal x
        x += 2
        print(x)
    f2()
f1()