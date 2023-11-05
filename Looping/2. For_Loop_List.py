# 1. Traverce through a list
# l = ['python', 10, 3.2,'java']
# for item in l:
#      print(item)

#or
# for index in range(len(l)):
#     print(index, l[index])


# 2. wap to print index and its corresponding item in the list
# l = ['python', 10, 3.2,'java']
# for item, index in enumerate(l):
#     print(index, item)

# for item in range (0,len(l)):
#     print(item, l[item])

# 3. wap to print elements in the list in reverse order
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

# 4. wap to print alternate elements in a list
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

# 5. wap to print integers present in the list
# l = ['python', 10, 3.2, 'selenium', 'java']

#using isinstance function
# for item in l:
#     if isinstance(item, int):
#         print(item)

# 6. print all numeric datatypes by using isinstance
# l = ['python', 10, 3.2, 'selenium', 1+5j, True, 'java']
# for item in l:
#     if isinstance(item, (int, float, complex)):
#         print(item)

# 7. wap to print length of each string in the list
# l = ['python', 'selenium', 'java']
# for item in l:
#     print(item, len(item))

# 8. wap to print the strings which are of even length in the list
# l = ['python', 'selenium', 'True', 'java', 'sri', 'for']
# for item in l:
#     if len(item) % 2 ==0:
#         print(item,len(item))

# 9. wap to print the strings which are of odd length in the list
# l = ['python', 'selenium', 'True', 'java', 'sri', 'for']
# for item in l:
#     if len(item) % 2 == 1:
#         print(item,len(item))

# 10. wap print to create a list which are even length string  (store inside list)
# l = ['python', 'selenium', 'True', 'java', 'sri', 'for']
# d = []
# for item in l:
#     if len(item) % 2 == 0:
#         d.append(item)
# print(d)

# 11. wap to print the elements in the list if the element is of even length print as it is, if it is odd then reverse and print
# l = ['python', 'selenium', 'True', 'java', 'sri', 'for']
# for item in l:
#     if len(item) % 2 == 0:
#         print(item)
#     else:
#         print(item[::-1])

# 12. wap to print the elements in the list if the element is of even length store inside list
# l = ['python', 'selenium', 'True', 'java', 'sri', 'for']
# d = []
# for item in l:
#     if len(item) % 2 == 0:
#         d.append(item)
#     else:
#         d.append(item[::-1])
# print(d)


# 13. wap to reverse the elements inside the list if the elements of type string or else keep it as it is
# l = ['python', 10, 2.2, True, 'selenium', 'True', 'java', 'sri', 'for']
# sl = []
# for item in l:
#     if isinstance(item, str):
#         sl.append(item[::-1])
#     else:
#         sl.append(item)
# print(sl)


# 14. wap to print the element which have starting with vowel
# files = ["Amezon", "Flipcart", "walmart", "gmail", "yahoo"]
# for item in files:
#     if item[0] in 'AEIOUaeiou':
#         print(item)


# 15. wap print all the extensions in the followig list
# files = ['youtube.txt', 'amazon.pdf', 'apple.xls', 'flipcart.in']
# l1 = []
# for item in files:
#     print(item.split('.')[1])

# 16. wap to print the file name if the file name is of odd length
# files = ['youtube.txt', 'amazon.pdf', 'apple.xls', 'flipkart.in']
#
# for item in files:
#     a = item.split('.')
#     if len(a[0]) % 2 == 0:
#         pass                #pass
#     else:
#         print(a[0])


# 17. wap to return index of the first occurrence of the given element
# number = [10, 20, 30, 40, 50, 40, 80, 30]
# num = 80

# using index
# print(number.index(num))

# 18. using 'break' statement
# for index, item in enumerate(number):
#     if item == num:
#         print(num, 'present in the', index)
#         break                                   #break
# else:
#     print('element is not found')

# 19. wap to print all the elements other than given element
# number = [10, 20, 30, 40, 50, 40, 30]
# n = 20
# for num in number:
#     if n == num:
#         continue
#     print(num)

# 20. wap print all the palindrome in the given list
# l = ['python', 'dad', 'hai', 'malayalam', 'madam', 'mom']
# for item in l:
#     if item == item[::-1]:
#         print(item)
