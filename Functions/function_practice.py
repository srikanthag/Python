#string

#waf to print index and the element in a string
# s = 'srikanth'
# def index_ele(argu):
#     for item, index in enumerate(argu):
#         print(item, index)
# index_ele(s)


# index_ele('srikanth')

#waf to traverce through a string in reverce order
# def rev_str(argu):
#     print(argu[::-1])
#
# rev_str('srikanth')

'''or'''

# def rev_str(argu):
#     return argu[::-1]
#
# print(rev_str('sri'))

##wap to count the number of characters present in the given string with out using len function
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


##waf to print even index characters in the string
# def even_index(arg):
#     return arg[0::2]
# print(even_index('srikanth'))

#waf to print the digit present inside string
# def digit(arg):
#     for num in arg:
#         if num.isdigit():
#             print(num, end=',')
# digit('srik1245563456')

##waf to count the number of digit present in the string
# def digit(arg):
#     count = 0
#     for num in arg:
#         if num.isdigit():
#             count += 1
#     return count
# print(digit('ser12389'))

#wap to count the number of special character present in the string
# def sp_char(arg):
#     count = 0
#     for char in arg:
#         if not ('0' <= char <= '9' or 'a' <= char <= 'z' or 'A' <= char <= 'Z'):
#             count += 1
#     return count
# 
# print(sp_char('sri@!#$123'))

#print tuple of char and its ascii value
# def tup_char(arg):
#     return arg, ord(arg)
# print(tup_char('s'))

#wap to print the sum of all digit present in string
# def sum_char(arg):
#     sum = 0
#     for num in arg:
#         if num.isdigit():
#             sum += int(num)
#     return sum
#
#
# print(sum_char('ser1234'))

#wap to print all the consonents present in the string and conunt of it
# def cosonent(arg):
#     count = 0
#     for item in arg:
#         if item.lower() not in 'aeiou':
#             count += 1
#     return count
#
# print(cosonent('srikan'))

##wap to print a tuple of index and its item in the string
# def in_it(arg):
#     for item, index in enumerate(arg):
#         print((item, index))
#
# in_it('sri')

##wap to check the if the given charracter present in string if it present return its index
# def str(arg):
#     char = 's'
#     for item in range(0, len(arg)):
#         if char == arg[item]:
#             print(arg[item], item)
# str('riksa')

#or
# def str(arg):
#     char = 's'
#     for item, index in enumerate(arg):
#         if char == index:
#             print(index, item)
# str('riksa')
# list

#Traverce through a list
# def list(arg):
#     return arg
# print(list([1,2,3,'sr']))

#wap to print index and its corresponding item in the list
# def list(arg):
#     for index, item in enumerate(arg):
#         print(item, index)
# list([1,2,3, 'srikanth'])


#wap to print elements in the list in reverce order
# def list(arg):
#     return arg[::-1]
# print(list([1,2,3,4]))

##wap to print integers present in the list
# def list(arg):
#     l = []
#     for item in arg:
#         if isinstance(item, int):
#             l.append(item)
#     print(l)
#
# list([1, 2, 1.5, 'sr'])

#print all numeric datatypes by using isinstance
# def list(arg):
#     l = []
#     for item in arg:
#         if isinstance(item, (int, float, complex)):
#             l.append(item)
#     print(l)
#
# list(['python', 10, 3.2, 'selenium', 1+5j, True, 'java'])


#wap to print length of each string in the list
# def list(arg):
#     for item in arg:
#         print(item, len(item))
# list(['python', 'selenium', 'java'])

#wap to print the strings which are of even length in the list
# def list(arg):
#     for item in arg:
#         if len(item) % 2 == 0:
#             print([item, len(item)])
# list(['python', 'selenium', 'jav'])

#wap to print the elements in the list if the element is of even length print as it is, if it is odd then
# reverse and print
# def list(arg):
#     for item in arg:
#         if len(item) % 2 == 0:
#             print(item, len(item))
#         else:
#             print(item[::-1], len(item))
# list(['python', 'selenium', 'jav'])

#wap to print the elements in the list if the element is of even length store inside list
# def list(arg):
#     l = []
#     for item in arg:
#         if len(item) % 2 == 0:
#             l.append(item)
#     return l
#
# print(list(['python', 'selenium', 'jav']))

#wap to reverse the elements inside the list if the elements of type string or else keep it as it is
# def list(arg):
#     l = []
#     for item in arg:
#         if isinstance(item, str):
#             l.append(item[::-1])
#     return l
#
# print(list(['python', 'selenium', 'jav', 10, 1.2, True]))

##wap to print the element which have starting with vowel
# def list(arg):
#     l = []
#     for item in arg:
#         if item[0].lower() in 'aeiou':
#             l.append(item)
#     return l

# print(list(["Amezon", "Flipcart", "ewalmart", "gmail", "yahoo"]))

#wap print all the extensions in the followig list
# def list(arg):
#     for item in arg:
#         print(item.split('.')[1])
# list(['youtube.txt', 'amazon.pdf', 'apple.xls', 'flipcart.in'])

#wap print all the paliondrome in the given list
# def list(arg):
#     for item in arg:
#         if item == item[::-1]:
#             print(item)
# list(['python', 'dad', 'hai', 'malayalam', 'madam', 'mom'])


#set

# wap to traverse through set and print each element
# def set(arg):
#     for item in arg:
#         print(item)
# set({'python', 'dad', 'hi'})

#dictionary
#wap to create a dictionary with the character and its count pair in a string
# def dict(arg):
#     d = {}
#     for item in arg:
#         d[item] = arg.count(item)
#     return d
# print(dict("srikaainth"))


#wap to create a dictionary with word and its count pair
# def dict(arg):
#     d = {}
#     sp = arg.split()
#     for word in sp:
#         d[word] = sp.count(word)
#     print(d)
# dict('hi how are')

#wap to reverse the values in the dictionary if the value is of type string
# def dict(d):
#     for key, value in d.items():
#         if isinstance(value, str):
#             d[key] = value[::-1]
#     print(d)
# dict({'a': 'hello', 'b': 100, 'c': 10.2, 'd': 'world'})

#wap to get duplicate items and the number of times the repeated in the list
# def dict(arg):
#     d = {}
#     for item in arg:
#         count = arg.count(item)
#         if count > 1:
#             d[item] = count
#     print(d)
# dict(['apple', 'google', 'yahoo', 'gamil', 'apple', 'gmail', 'google'])

#wap to create a dictionary to count the no of occurance of each char
# def dict(arg):
#     d = {}
#     for char in arg:
#         d[char] = arg.count(char)
#     print(d)
# dict('srikanthh')
