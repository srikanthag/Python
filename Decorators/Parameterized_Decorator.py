
# 1. wad which execute a function for n times
# def outer(n):
#     def str_rev(func):
#         def wrapper(*args, **kwargs):
#             for i in range(4):
#                 func(*args, **kwargs)
#         return wrapper
#     return str_rev
#
#
# @outer(4)
# def sub(a, b):
#     print(a-b)
# sub(1,2)
#

# 2. wad print "hello world" message if the user has not given input
# def outer(n='krishna'):
#     def msg(func):
#         def wrapper(*args, **kwargs):
#             print(n)
#             func(*args, **kwargs)
#         return wrapper
#     return msg
#
# @outer()
# def sub(a, b):
#     print(a-b)
# sub(2,1)


#phone decorator                            #incomplete
# numbers = [1234567890, 9087654321, 911234567890, 119876543210]
# def add_prefix(number):
#     str_number = str(number)
#     if len(str_number) == 10:
#         str_number =="+91" + str_number
#         return str_number
#     elif len(str_number)





