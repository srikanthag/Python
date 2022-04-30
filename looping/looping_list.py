#Traverce through a list
# l = ['python', 10, 3.2,'java']
# for item in l:
#      print(item)

#or
# for index in range(len(l)):
#     print(index, l[index])


#wap to print index and its corresponding item in the list
# l = ['python', 10, 3.2,'java']
# for item, index in enumerate(l):
#     print(index, item)

# for item in range (0,len(l)):
#     print(item, l[item])

#wap to print elements in the list in reverce order
# l = ['python', 10, 3.2,'java']

#using range function
# for item in range (len(l) -1, -1, -1):
#     print(l[item], end=',')
#
#using slicing method
# for item in l[::-1]:
#     print(item, end='')
#
#using reversed function
# for item in reversed(l):
#     print(item)


#wap to print alternate elements in a list
# l = ['python', 10, 3.2, 'selenium', 'java']

#range function
# for item in range (0, len(l), 2):
#     print(l[item])

#slicing method
# for item in l[::2]:
#     print(item)

#use condition (odd index)
# for i in range (len(l)):
#     if i % 2 == 1:
#         print(l[i])

#use condition (even index)
# for i in range (len(l)):
#     if i % 2 == 0:
#         print(l[i])

#wap to print integers present in the list
# l = ['python', 10, 3.2, 'selenium', 'java']

#using isinstance function
# for item in l:
#     if isinstance(item, int):
#         print(item)

#print all numeric datatypes by using isinstance
# l = ['python', 10, 3.2, 'selenium', 1+5j, True, 'java']
# for item in l:
#     if isinstance(item, (int, float, complex)):
#         print(item)


#wap to print length of each string in the list
# l = ['python', 'selenium', 'java']
# for item in l:
#     print(item, len(item))

#wap to print the strings which are of even length in the list
# l = ['python', 'selenium', 'True', 'java', 'sri', 'for']
# for item in l:
#     if len(item) % 2 ==0:
#         print(item,len(item))

#wap to print the strings which are of odd length in the list
# l = ['python', 'selenium', 'True', 'java', 'sri', 'for']
# for item in l:
#     if len(item) % 2 == 1:
#         print(item,len(item))

#wap print to create a list which are even length string  (store insde list)
# l = ['python', 'selenium', 'True', 'java', 'sri', 'for']
# d = []
# for item in l:
#     if len(item) % 2 == 0:
#         d.append(item)
# print(d)

# wap to print the elements in the list if the element is of even length print as it is, if it is odd then
# reverse and print
# l = ['python', 'selenium', 'True', 'java', 'sri', 'for']
# for item in l:
#     if len(item) % 2 == 0:
#         print(item)
#     else:
#         print(item[::-1])

# wap to print the elements in the list if the element is of even length store inside list
# l = ['python', 'selenium', 'True', 'java', 'sri', 'for']
# d = []
# for item in l:
#     if len(item) % 2 == 0:
#         d.append(item)
#     else:
#         d.append(item[::-1])
# print(d)


#wap to reverse the elements inside the list if the elements of type string or else keep it as it is
# l = ['python', 10, 2.2, True, 'selenium', 'True', 'java', 'sri', 'for']
# sl = []
# for item in l:
#     if isinstance(item, str):
#         sl.append(item[::-1])
#     else:
#         sl.append(item)
# print(sl)


#wap to print the element which have starting with vowel
# files = ["Amezon", "Flipcart", "walmart", "gmail", "yahoo"]
# for item in files:
#     if item[0] in 'AEIOUaeiou':
#         print(item)


#wap print all the extensions in the followig list
# files = ['youtube.txt', 'amazon.pdf', 'apple.xls', 'flipcart.in']
# l1 = []
# for item in files:
#     print(item.split('.')[1])

#wap to print the file name if the file name is of odd length
# files = ['youtube.txt', 'amazon.pdf', 'apple.xls', 'flipcart.in']
#
# for item in files:
#     a = item.split('.')
#     if len(a[0]) % 2 == 0:
#         pass                #pass
#     else:
#         print(a[0])


#wap to return index of the first occurance of the given element
# number = [10, 20, 30, 40, 50, 40, 80, 30]
# num = 80

# using index
# print(number.index(num))

#using 'break' statement
# for index, item in enumerate(number):
#     if item == num:
#         print(num, 'present in the', index)
#         break                                   #break
# else:
#     print('element is not found')

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


#wap to print all the elements other than given element
# number = [10, 20, 30, 40, 50, 40, 30]
# n = 20
# for num in number:
#     if n == num:
#         continue
#     print(num)

# to print the prime number in the given sequence
# l = [1, 2, 3, 4, 5, 6, 98, 45]
# for item in l:
#     if item > 1:
#         for i in range(2, item):
#             if item % i == 0:
#                 print(item, 'not a prime number')
#                 break
#         else:
#             print(item, 'prime number')


#wap print all the paliondrome in the given list
# l = ['python', 'dad', 'hai', 'malayalam', 'madam', 'mom']
# for item in l:
#     if item == item[::-1]:
#         print(item)