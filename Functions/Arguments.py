# 1. waf tha returns the number of positional arguments that are given to the function
# def count(*args):
#     return len(args)
#
# print(count(1, 2, 3))

#or
# def fun(*args):
#     count = 0
#     for _ in args:
#         count += 1
#     return count
# print(fun(1,2,3,4))

# 2. waf that takes variable number of positional arguments and return all iteger values
# def int_data(*args):
#     for item in args:
#         if isinstance(item, int):
#             print(item)
#
# int_data(1, 2, 3, 3.5, True)


# 3. waf tah takes multiple arguments and returns the string in reversed order

# def str_data(*args):
#     for item in args:
#         if isinstance(item, str):
#             print(item[::-1])
#
# str_data(1, 2, 'sri', 'kanth', 3, 3.5, True)


# 4. waf that reurns no of positional arguments and number of keyword arguments
# def count_(*args, **kwargs):
#     return len(args), len(kwargs)
#
# print(count_(1, 2, 3, a=10, b=20, c=30))


# 5. waf that checks if the given number of argument greate than 5 or not
# def gret(*args):
# d = 'srikanth'
#     if len(args) > 5:
#         return 'number argument greater than 5'
#     else:
#         return 'numbers are less than 5'

# print(gret(2,5,6,7,7,8))
