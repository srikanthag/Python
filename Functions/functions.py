#only print result in the function bocy
# def spam(val1, val2):
#     a = val1
#     b= val2
#     c = a + b
#     print(c)

# print(spam)

#returning the value from the function
# def spam(val1, val2):
#     a = val1
#     b= val2
#     c = a + b
#     return c
# print(spam(2, 4))

#store
# res = spam(2, 4)
# print(res)

#return statements multiple values
# def function(a, b):
#     print(a, b)
#     return a, b
#
# res = function(1, 2)
# print(res)

#return statements single values
# def f1(a):
#     return a
# print(f1('srikanth'))


#arguments
#positional arguments

# def greet(name, age):
#     print(f"{name} is {age} year old")

# greet("srikanth", 34)
# greet(34, "srikanth")

#keyword arguments
# def greet(name, age):
#     print(f"{name} is {age} year old")
#
# greet(name="srikanth", age= 20)
# greet(age= 20, name="srikanth")

##combination of keyword and positional arguments
# def add_(a, b, c, d):
#     print(a, b, c, d)
#
# add_(1, 2, 3, 4)
# add_(a=1, b=2, c=3, d=4)
# add_(1, 2, c=3, d=4)
# add_(a=1, b=2, 3, 4)   #syntax error

#positional only arguments
# def add_(a, b, c, d, /):
#     print(a, b, c, d)

#add_(1,2,3,4)
#add_(a=1, b=2, c=3, d=4)


# def add_(a, b, /, c, d, ):
#     print(a, b, c, d)
# add_(1, 2, c=3, d=4)
# add_(1, b=2, 3, 4)

#keyword only arguments
# def add_(*, a, b, c, d, ):
#     print(a, b, c, d)
# add_(a=1, b=2, c=3, d=4)
# add_(1, b=2, c=3, d=4)

# def add_(a, b, *, c, d):
#     print(a, b, c, d)
# # add_(a=1, b=2, c=3, d=4)
# add_(1, 2, c=3, d=4)
# add_(1, 2, 3, d=4) #type erroe
#

#using * and /
# def add_(a, b, /, *, c, d):
#     print(a,b,c,d)
# add_(1,2,c=3,d=4)


#w a function to add two numbers and return the result
# def add_(a,b):
#     c = a + b
#     return c


# z = add_(1,2)
# print(z)

#use positional or keyword arguments
# def add_(a,/,*,b):
#     print(a,b)
#
#
# add_(1, b=2)

#use positional arguments
# def add_(a,b,/):
#     print(a,b)


# add_(1, 2)

#only keyword arguments
# def add_(*, a ,b):
#     print(a, b)


# add_(a=1, b=2)


#wa function which returns list even numbers from the range 1 to 50 in ythe given range
# def evens(end, start=0):
#     l = []
#     for i in range(start, end):
#         if i % 2 == 0:
#             l.append(i)
#     return l
# print(evens(21))
# print(evens(21, 5))


#default parameters
# def add_(a,b,c=0):
#     return a+b+c
#
# print(add_(10, 20))


#
# x = 20
# def add_(a, b=x):
#     print(a + b)
#
# x = 20
# add_(10)

#wa function that returns all the prime numbers in user defined range if the user doesnot start index take it a 2
# and create a list
# def prime(end, start = 2):
#     l = []
#     for n in range(start, end + 1):
#         if n > 1:
#             for i in range(2, n):
#                 if n % i == 0:
#                     break
#             else:
#                 l.append(n)
#     return l
# print(prime(start=1, end=30))


#waf to print fibonacci seris in the user defined range
# def fib(end, start=0):
#     a = 0
#     b = 1
#     i = 0
# while i < end:
#         c = a + b
#         a = b
#         b = c
#         i += c
#     return a
# print(fib(10))


#wa function that returs fibonocii seris upto the number specified




#wa function that returns n th febonocii number




#variable positional arguments
# def spam(*args):           #packing
#     print(args)
#
# spam(1, 2, 3)


#wa function that is integers and float datatypes as input or aguments and returns its sum
# def sum_(*args):
#     print(args)
#     print(sum(args))
#
# sum_(2, 4)

#or
# total = 0
# for i in args:
#     total += i
# print(total)

#or
# for i in args:
#     if isinstance(i,(int, float)):
#         total += i
# print(sum_(1,2))


#waf tha returns the number of positional arguments that are given to the function
# def count(*args):
#     return len(args)
#
#
# print(count(1, 2, 3))

#or
# def fun(*args):
#     count = 0
#     for _ in args:
#         count += 1
#     return count
# print(fun(1,2,3,4))

#waf that takes variable number of positional arguments and return all iteger values
# def int_data(*args):
#     for item in args:
#         if isinstance(item, int):
#             print(item)
#
# int_data(1, 2, 3, 3.5, True)
#

#waf tah takes multiple arguments and returns the string in reversed order

# def str_data(*args):
#     for item in args:
#         if isinstance(item, str):
#             print(item[::-1])
#
#
# str_data(1, 2, 'sri', 'kanth', 3, 3.5, True)

#variable keyword arguments

# def keyword_arg(**kwargs):
#     return kwargs
#
# keyword_arg(a=1, b= 2, c=3)

#waf that reurns no of positional arguments and number of keyword arguments
# def count_(*args, **kwargs):
#     return len(args), len(kwargs)
#
# print(count_(1, 2, 3, a=10, b=20, c=30))

#waf that checks if the given number of a
# def gret(*args):gruments is greate than 5 or not
# # d = 'srikanth'
#     if len(args) > 5:
#         return 'number argument greater than 5'
#     else:
#         return 'numbers are less than 5'

# print(gret(2,5,6,7,7,8))


#write a function to print message 'hai everyone' if the user input is not present  and if user input present print the user input
# def spam(msg= 'hi everyone'):
#     print(msg)
#
#
# spam('hello')
# spam()

# num = 10
# def add(b, a=num):
#     return a+b
#     a = 30
# print(add(35))      #it accept only global variabe

# def add(a,b):
#     add.count = add.count + 1
#     return a+b
#
# def sub(a,b):
#     sub.count = sub.count + 1
#     return a+b
#
# add.count = 0
# sub.count = 0
# item = [1,2,add,sub]



























