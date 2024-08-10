# 1. wad which execute a function for n times
def outer(n):
    def str_rev(func):
        def wrapper(*args, **kwargs):
            for i in range(4):
                func(*args, **kwargs)
        return wrapper
    return str_rev

@outer(4)
def sub(a, b):
    print(a-b)
sub(1,2)


# 2. wad print "hello world" message if the user has not given input
def outer(n='krishna'):
    def msg(func):
        def wrapper(*args, **kwargs):
            print(n)
            func(*args, **kwargs)
        return wrapper
    return msg

@outer()
def sub(a, b):
    print(a-b)
sub(2,1)
