# Fibonacci series
# The Fibonacci series in python is a mathematical sequence that starts with 0 and 1,
# with each subsequent number being the sum of the two preceding ones.


#1, febnocii number seris
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

#7. waf that checks if the given number is fibonocii number or not
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




# Prime number

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



#prime numbers

#print whether prime or not
# n = 10
# for item in range(2, n):
#     if n % item == 0:
#         print('not a prime number')
#         break
# else:
#     print('prime number')

#genarate seris of prime number

# for n in range(15):
#     if n > 1:
#         for item in range(2, n):
#             if n % item == 0:
#                 break
#         else:
#             print(n)

# 20. wap to print the prime number in the given sequence
# l = [1, 2, 3, 4, 5, 6, 98, 45]
# for item in l:
#     if item > 1:
#         for i in range(2, item):
#             if item % i == 0:
#                 print(item, 'not a prime number')
#                 break
#         else:
#             print(item, 'prime number')
