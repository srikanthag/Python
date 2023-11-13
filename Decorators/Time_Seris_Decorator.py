# 1. wad which inputs delay of n seconds
# import time
# def outer(n):
#     def delay(func):
#         def wrapper(*args, **kwargs):
#             time.sleep(n)
#             func(*args, **kwargs)
#         return wrapper
#     return delay
#
# @outer(3)
# def add(a,b):
#     print(a+b)
# add(1,3)
#
# @outer(5)
# def add(a,b):
#     print(a-b)
# add(1,3)


# 2. execution time of the function

# from time import time, sleep
# def delay(func):
#     def wrapper(*args, **kwargs):
#         start = time()
#         result = func(*args, **kwargs)
#         end = time()
#         print(f"execution of function {func.__name__} {end-start} seconds")
#         return result
#     return wrapper
#
# @delay    #display = log(display)
# def greet():
#     return "hello world"
# print(greet())
#
# @delay
# def add(a,b):
#     print(a+b)
# add(1,3)
#
# @delay
# def sub(c,d):
#     print(c-d)
# sub(10,-30)
#
# @delay
# def mul(a, b):
#     print(a * b)
# mul(10, 30)


# 3. wad function that calculates time of execution of a function
# import time
# def outer(n):
#     def delay(func):
#         def wrapper(*args, **kwargs):
#             start = time.time()
#             time.sleep(n)
#             func(*args, **kwargs)
#             end = time.time()
#             print(f"time of execution {end-start}")
#         return wrapper
#     return delay
#
# @outer(3)
# def add(a,b):
#     print(a+b)
# add(1,3)
#
# @outer(5)
# def add(a,b):
#     print(a-b)
# add(1,3)

