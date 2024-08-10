# 1. wa decorator that prints or that logs a message before execution any function
def log (func):
    def wrapper(*args, **kwargs):
        print("in decorator function")
        return func(*args, **kwargs)
    return wrapper

@log    # display = log(display)
def display():
   return "in display"
print(display())


# 2. wa decorator to convert lower case to upper
def upper(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res.lower():
            return res.upper()
    return wrapper

@upper
def greet():
    return "srikanth"
print(greet())


# 3. wad to input some delay before executing any function
import time
def delay(func):
    def wrapper(*args, **kwargs):
        time.sleep(2)
        return func(*args, **kwargs)
    return wrapper

@delay
def display():
    return 'its delay'
print(display())


# 4. wad which takes a string and reversed
def str_rev(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        for item in res:
            if isinstance(item, str):
                return res[::-1]
    return wrapper

@str_rev
def spam(string):
    return string
print(spam('hello world'))


# 5. wad to execute a function for 3 times
def str_rev(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            func(*args, **kwargs)
    return wrapper

@str_rev
def add(a,b):
    print(a+b)
add(1,6)

@str_rev
def sub(a,b):
    print(a-b)
sub(1,6)

@str_rev
def mul(a,b):
    print(a*b)
mul(2,6)


# 6. wad function to count the number of arguments passed to a function
def count(func):
    def wrapper(*args, **kwargs):
        print(len(args))
        func(*args, **kwargs)
    return wrapper

@count
def add(a, b):
    print(a + b)
add(1, 2)


# 7. wad to return only positive value after subtraction
def positive(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return abs(res)               #conversion result
        return res                    #normal result
    return wrapper

@positive
def sub(a, b):
    return a-b
print(sub(5,7))

# 8. wad to reverse the value if it is string
def reverse (func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result[::-1]
        return result
    return wrapper

@reverse
def greet():
    return "hello world"
print(greet())

@reverse
def add(a,b):
    print(a+b)
add(1,3)

@reverse
def sub(a,b):
    print(a-b)
sub(1,3)


# 9. if positive return positive if negative abs of result
def positive (func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, int):
            return abs(result)
        return result
    return wrapper

@positive
def greet():
    return "hello world"
print(greet())

@positive
def add(a,b):
    return a+b
print(add(1,3))

@positive
def sub(a,b):
    return a-b
print(sub(1,3))


# 10. wad function count the number of calls     #confuse
from collections import defaultdict
count_ = defaultdict(int)
def func_count(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        count_[func.__name__] = 1
        return res
    return wrapper

@func_count
def greet():
    return "hello world"
print(greet())

@func_count
def add(a,b):
    return a+b
print(add(1,3))

@func_count
def sub(c,d):
    return c-d
print(sub(10,-30))

@func_count
def mul(a, b):
    return a * b
print(mul(10, 30))

# 11. cache the argument and return dictionary
def cache_(func):
    d = {}
    def wrapper(*args, **kwargs):
        if args not in d:
            result = func(*args, **kwargs)
            d[args] = result
            return result
        print('result')
        return d[args]

    return wrapper

@cache_
def add(a,b):   #add = log(add)
    return a+b
print(add(1,3))
