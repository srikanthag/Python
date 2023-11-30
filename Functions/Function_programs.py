# 1. waf to check whether the number is prime or not
# def prime(num):
#     for item in range(2, num):
#         if num % item == 0:
#             return 'not prime number'
#     return 'prime number'
#
# print(prime(9))


# 2. waf to written last digit of num
# def last(num):
#     num1 = str(num)
#     for item in num1:
#         return num1[-1]
#
# print(last(123546))

#or
# def last(num):
#     return num % 10   #returns str(num)[-1]
# print(last(123546))


# 3. wap named tail that takes sequence as input and a number n and returns the last n element as the sequence
# def tail(sequence, n):
#     return sequence[-n:]
# print(tail('hello', 2))

# 4. waf name is perfect square and that accept number and returns true if it is a perfect squre and retuens false if it is not
# def is_perfectsqr(num):
#     a = int(num ** 0.5)
#     if a * a == num:
#         return True
#     return False
# print(is_perfectsqr(25))

# or

# def is_perfectsqr(num):
#     for i in range(num):
#         if i ** 2 == num:
#             return True
#     return False
# print(is_perfectsqr(24))

# or
# n = 16
# a = n**0.5
# if a**2 == n:
#     print('yes')
# else:
#     print('no')

# 5. waf to get the below output
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


# 6. waf that takes variable number of inputs and returns length of all the iterable given
# def len_var(*args):
#     for item in args:
#         if isinstance(item, (str, tuple, list, set, dict)):
#             print(list(item), len(item))
#
# len_var('sri', [1,2,3])

# 7. waf to print 1 to 10
# def count_10(start, end):
#     for i in range(start, end+1):
#         print(i)
# count_10(20, 44)

# 8. Anagrams
# def str_(a,b):
#     a = sorted(a)
#     b = sorted(b)
#     if a == b:
#         return True
#     else:
#         return False
#
# print(str_('eat', 'tea'))


# 8. only print result in the function body
# def spam(val1, val2):
#     a = val1
#     b = val2
#     c = a + b
#     print(c)

# print(spam)

# 9. returning the value from the function
# def spam(val1, val2):
#     a = val1
#     b = val2
#     c = a + b
#     return c
# print(spam(2, 4))

# store
# res = spam(2, 4)
# print(res)

# 10. return statements multiple values
# def function(a, b):
#     print(a, b)
#     return a, b
#
# res = function(1, 2)
# print(res)

# 11. return statements single values
# def f1(a):
#     return a
# print(f1('srikanth'))

# 12. wa function to add two numbers and return the result
# def add_(a,b):
#     c = a + b
#     return c

# z = add_(1,2)
# print(z)

# 13. wa function which returns list even numbers from the range 1 to 50 in the given range
# def evens(end, start=0):
#     l = []
#     for i in range(start, end):
#         if i % 2 == 0:
#             l.append(i)
#     return l
# print(evens(21))
# print(evens(21, 5))

# 14. wa function that is integers and float datatypes as input or aguments and returns its sum
# def sum_(*args):
#     i = 0
#     for item in args:
#         if isinstance(item, (int, float)):
#             i += item
#     return i
# print(sum_(1,5))

#15. write a function to print message 'hai everyone' if the user input is not present  and if user input present print the user input
# def spam(msg= 'hi everyone'):
#     print(msg)
# spam('hello')
# spam()

# 16. Waf to accept global variable in the functions
# num = 10
# def add(b, a=num):
#     return a+b
#     a = 30
# print(add(35))      #it accept only global variabe

# ====================================================================================================

#string#

# 17. waf to print index and the element in a string
# s = 'srikanth'
# def index_ele(argu):
#     for item, index in enumerate(argu):
#         print(item, index)
# index_ele(s)
# index_ele('srikanth')

# 18. waf to traverse through a string in reverse order
# def rev_str(argu):
#     print(argu[::-1])
#
# rev_str('srikanth')

# 19. wap to count the number of characters present in the given string with out using len function
# def coun_str(arg):
#     d = {}
#     for item in arg:
#         count = 0
#         for j in arg:
#             if item == j:
#                 count += 1
#         print(d[item] = count)
#
# print(coun_str('ss112ri'))

# 20. waf to print even index characters in the string
# def even_index(arg):
#     return arg[0::2]
# print(even_index('srikanth'))

# 21. waf to print the digit present inside string
# def digit(arg):
#     for num in arg:
#         if num.isdigit():
#             print(num, end=',')
# digit('srik1245563456')

# 22. waf to count the number of digit present in the string
# def digit(arg):
#     count = 0
#     for num in arg:
#         if num.isdigit():
#             count += 1
#     return count
# print(digit('ser12389'))

# 23. wap to count the number of special character present in the string
# def sp_char(arg):
#     count = 0
#     for char in arg:
#         if not ('0' <= char <= '9' or 'a' <= char <= 'z' or 'A' <= char <= 'Z'):
#             count += 1
#     return count
#
# print(sp_char('sri@!#$123'))

# 24. print tuple of char and its ascii value
# def tup_char(arg):
#     return arg, ord(arg)
#
# print(tup_char('s'))

# 25. wap to print the sum of all digit present in string
# def sum_char(arg):
#     sum = 0
#     for num in arg:
#         if num.isdigit():
#             sum += int(num)
#     return sum
#
# print(sum_char('ser1234'))

# 26. wap to print all the consonants present in the string and count of it
# def consonants(arg):
#     count = 0
#     for item in arg:
#         if item.lower() not in 'aeiou':
#             count += 1
#     return count
#
# print(consonants('srikan'))

# 27. wap to print a tuple of index and its item in the string
# def in_it(arg):
#     for item, index in enumerate(arg):
#         print(item, index)
#
# in_it('sri')

# 28. wap to check the if the given charracter present in string if it present return its index
# def str(arg):
#     char = 's'
#     for item, index in enumerate(arg):
#         if char == index:
#             print(index, item)
# str('riksa')


# ===================================================================================================

#List#

# 29. Traverse through a list
# def list(arg):
#     return arg
# print(list([1,2,3,'sr']))

# 30. wap to print index and its corresponding item in the list
# def list(arg):
#     for index, item in enumerate(arg):
#         print(item, index)
# list([1,2,3, 'srikanth'])

# 31. wap to print elements in the list in reverse order
# def list(arg):
#     return arg[::-1]
# print(list([1,2,3,4]))

# 32. wap to print integers present in the list
# def list(arg):
#     l = []
#     for item in arg:
#         if isinstance(item, int):
#             l.append(item)
#     print(l)
#
# list([1, 2, 1.5, 'sr'])

# 33. print all numeric data types by using isinstance
# def list(arg):
#     l = []
#     for item in arg:
#         if isinstance(item, (int, float, complex)):
#             l.append(item)
#     print(l)
#
# list(['python', 10, 3.2, 'selenium', 1+5j, True, 'java'])

# 34. wap to print length of each string in the list
# def list(arg):
#     for item in arg:
#         print(item, len(item))
# list(['python', 'selenium', 'java'])

# 35. wap to print the strings which are of even length in the list
# def list(arg):
#     for item in arg:
#         if len(item) % 2 == 0:
#             print([item, len(item)])
# list(['python', 'selenium', 'jav'])

# 36. wap to print the elements in the list if the element is of even length print as it is, if it is odd then
# reverse and print
# def list(arg):
#     for item in arg:
#         if len(item) % 2 == 0:
#             print(item, len(item))
#         else:
#             print(item[::-1], len(item))
# list(['python', 'selenium', 'jav'])

# 37. wap to print the elements in the list if the element is of even length store inside list
# def list(arg):
#     l = []
#     for item in arg:
#         if len(item) % 2 == 0:
#             l.append(item)
#     return l
#
# print(list(['python', 'selenium', 'jav']))

# 38. wap to reverse the elements inside the list if the elements of type string or else keep it as it is
# def list(arg):
#     l = []
#     for item in arg:
#         if isinstance(item, str):
#             l.append(item[::-1])
#     return l
#
# print(list(['python', 'selenium', 'jav', 10, 1.2, True]))

# 39. wap to print the element which have starting with vowel
# def list(arg):
#     l = []
#     for item in arg:
#         if item[0].lower() in 'aeiou':
#             l.append(item)
#     return l

# print(list(["Amezon", "Flipcart", "ewalmart", "gmail", "yahoo"]))

# 40. wap print all the extensions in the following list
# def list(arg):
#     for item in arg:
#         print(item.split('.')[1])
# list(['youtube.txt', 'amazon.pdf', 'apple.xls', 'flipcart.in'])

# 41. wap print all the palindrome in the given list
# def list(arg):
#     for item in arg:
#         if item == item[::-1]:
#             print(item)
# list(['python', 'dad', 'hai', 'malayalam', 'madam', 'mom'])

# ================================================================================================

# Set #

# 41. wap to traverse through set and print each element
# def set(arg):
#     for item in arg:
#         print(item)
# set({'python', 'dad', 'hi'})

# ==================================================================================================

# Dictionary #

# 42. wap to create a dictionary with the character and its count pair in a string
# def dict(arg):
#     d = {}
#     for item in arg:
#         d[item] = arg.count(item)
#     return d
# print(dict("srikaainth"))

# 43. wap to create a dictionary with word and its count pair
# def dict(arg):
#     d = {}
#     sp = arg.split()
#     for word in sp:
#         d[word] = sp.count(word)
#     print(d)
# dict('hi how are')

# 44. wap to reverse the values in the dictionary if the value is of type string
# def dict(d):
#     for key, value in d.items():
#         if isinstance(value, str):
#             d[key] = value[::-1]
#     print(d)
# dict({'a': 'hello', 'b': 100, 'c': 10.2, 'd': 'world'})

# 45. wap to get duplicate items and the number of times the repeated in the list
# def dict(arg):
#     d = {}
#     for item in arg:
#         count = arg.count(item)
#         if count > 1:
#             d[item] = count
#     print(d)
# dict(['apple', 'google', 'yahoo', 'gamil', 'apple', 'gmail', 'google'])

# 46. wap to create a dictionary to count the no of occurrence of each char
# def dict(arg):
#     d = {}
#     for char in arg:
#         d[char] = arg.count(char)
#     print(d)
# dict('srikanthh')






