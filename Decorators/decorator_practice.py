'''decorators'''
# decorators takes in function add some functionality and return it

'''uses'''
# allow the extension of an existing function, without any modification to the original function source code.

#wa decorator that prints or that logs a message before executiong any function
# def log (func):
#     def wrapper(*args, **kwargs):
#         print("in decorator function")
#         return func(*args, **kwargs)
#     return wrapper

# @log    #display = log(display)
# def display():
#    return "in display"
# print(display())


#lower case to upper
# def upper(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         if res.lower():
#             return res.upper()
#     return wrapper
#
# @upper
# def greet():
#     return "srikanth"
# print(greet())

#wad to input some delay before executing any function
# import time
# def delay (func):
#     def wrapper(*args, **kwargs):
#         time.sleep(2)
#         return func(*args, **kwargs)
#     return wrapper
#
# @delay
# def display():
#     return 'its delay'
# print(display())

#wad which takes a string and reversed
# def str_rev(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         for item in res:
#             if isinstance(item, str):
#                 return res[::-1]
#     return wrapper
#
#
# @str_rev
# def spam(string):
#     return string
# print(spam('hello world'))

#wad to execute a function for 3 times

# def str_rev(func):
#     def wrapper(*args, **kwargs):
#         for i in range(3):
#             func(*args, **kwargs)
#     return wrapper
# @str_rev
# def add(a,b):
#     print(a+b)
# add(1,6)
#
# @str_rev
# def sub(a,b):
#     print(a-b)
# sub(1,6)
#
# @str_rev
# def mul(a,b):
#     print(a*b)
# mul(2,6)


#wad function to count the number of arguments passed to a function
# def count(func):
#     def wrapper(*args, **kwargs):
#         print(len(args))
#         func(*args, **kwargs)
#     return wrapper
# @count
# def add(a, b):
#     print(a + b)
# add(1, 2)


#wadf to return only possitive value after subtraction
# def positive(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return abs(res)               #conversion result
#         return res                    #normal result
#     return wrapper
#
# @positive
# def sub(a, b):
#     return a-b
# print(sub(5,7))

#reversed decorator
# def reverse (func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result, str):
#             return result[::-1]
#         return result
#     return wrapper
#
# @reverse
# def greet():
#     return "hello world"
# print(greet())
#
# @reverse
# def add(a,b):
#     print(a+b)
# add(1,3)
#
# @reverse
# def sub(a,b):
#     print(a-b)
# sub(1,3)

#if positive return positive if negetive abs of result
# def positive (func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result, int):
#             return abs(result)
#         return result
#     return wrapper
#
# @positive
# def greet():
#     return "hello world"
# print(greet())
#
# @positive
# def add(a,b):
#     return a+b
# print(add(1,3))
#
# @positive
# def sub(a,b):
#     return a-b
# print(sub(1,3))


#wad function count the number of calls     #confuse
# from collections import defaultdict
# count_ = defaultdict(int)
# def func_count(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         count_[func.__name__] = 1
#         return res
#     return wrapper
#
# @func_count
# def greet():
#     return "hello world"
# print(greet())
#
# @func_count
# def add(a,b):
#     return a+b
# print(add(1,3))
#
# @func_count
# def sub(c,d):
#     return c-d
# print(sub(10,-30))
#
# @func_count
# def mul(a, b):
#     return a * b
# print(mul(10, 30))


# max counts        #confuse

# def max(func):
#     func.count = 0
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         func.count += 1
#         if func.count > 1:
#             raise ValueError(f"max call{func.__name__} exceed")
#     return wrapper
#
# @max
# def greet():
#     return "hello world"
# print(greet())
#
# @max
# def add(a,b):
#     return a+b
# print(add(1,3))
#
# @max
# def sub(c,d):
#     return c-d
# print(sub(10,-30))

# @max
# def mul(a, b):
#     return a * b
# print(mul(10, 30))
#


# print log
# def log (func):
#     def wrapper(*args, **kwargs):            #original function exicuting add and greet
#         print(f"you calling {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper
#
# @log    #display = log(display)
# def greet():
#     print("hello world")
# greet()
#
# @log
# def add(a,b):   #add = log(add)
#     print(a+b)
# add(1,3)


#cache the argument and return dictionary
# def cache_(func):
#     d = {}
#     def wrapper(*args, **kwargs):
#         if args not in d:
#             result = func(*args, **kwargs)
#             d[args] = result
#             return result
#         print('result')
#         return d[args]
#
#     return wrapper
#
# @cache_
# def add(a,b):   #add = log(add)
#     return a+b
# print(add(1,3))


