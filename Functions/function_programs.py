#waf to check whether the number is prime or not
# def prime(num):
#     for item in range(2, num):
#         if num % item == 0:
#             return'prime not number'
#     return 'prime number'
#
# print(prime(9))

#waf to written last digit of num
# def last(num):
#     num1 = str(num)
#     for item in num1:
#         return num1[-1]
# print(last(123546))

#or
# def last(num):
#     return num % 10   #returns str(num)[-1]
# print(last(123546))

#wap named tail that takes sequence as input and a number n and returns the last n element as the sequence
# def tail(sequence, n):
#     return sequence[-n:]
# print(tail('hello', 2))

#waf name is perfect squre and that accept number and returns true if it is a perfect squre and retuens false if it is not
# def is_perfectsqr(num):
#     a = int(num ** 0.5)
#     if a * a == num:
#         return True
#     return False
# print(is_perfectsqr(25))

#or

# def is_perfectsqr(num):
#     for i in range(num):
#         if i ** 2 == num:
#             return True
#     return False
# print(is_perfectsqr(24))

'''or'''
# n = 16
# a = n**0.5
# if a**2 == n:
#     print('yes')
# else:
#     print('no')

#waf to get the below output
# func("TRACXN", 0)  #Print RCN
# func("TRACXN", 1)  #Print TAX
# def fun(string, num):
#     if num == 0:
#         return string[1::2]
#     elif num == 1:
#         return string[::2]
#     else:
#         return 'n value is invalid'
# print(fun("TRACXN", 1))

#febnocii number seris
# def febonocii(num):
#     a = 0
#     b = 1
#     i = 0
#     while i <= num:
#         print(a)
#         c = a + b
#         a = b
#         b = c
#         i += 1
# febonocii(3)

#waf that checks if the given number is fibonocii number or not
# def febonocii(num):
#     a = 0
#     b = 1
#     while a <= num:
#         c = a + b
#         a = b
#         b = c
#         if a == num:
#             print(num, 'is a febenocii number')
#             break
#     else:
#         print(num, 'not febenocii number')
# febonocii(10)

#waf fibonocii number up to given input

# def febt(10)

#waf that takes variable number of inputs and returns length of all the iterabled given
# def len_var(*args):
#     for item in args:
#         if isinstance(item, (str, tuple, list, set, dict)):
#             print(list(item), len(item))
#
# len_var('sri', [1,2,3])

#waf to print 1 to 10
# def count_10(start, end):
#     for i in range(start, end+1):
#         print(i)
# count_10(20, 44)

# import keyword
# print(keyword.kwlist)

#anagramous
# def str_(a,b):
#     a = sorted(a)
#     b = sorted(b)
#     if a == b:
#         return True
#     else:
#         return False
#
# print(str_('eat', 'tea'))









