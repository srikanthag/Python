# 1. traversing through string
# s = 'srikanth'
# for i in s:
#     print(i)

# 2. wap to print index and the element in a string

# string = 'srikanth'
# for item in range (0,len(string)):
#     print(item, string[item], sep='--')

# or
# for item in enumerate(string):
#     print(item[0],item[1])

# or
# for index, item in enumerate(s):
#     print(index,item)


# 3. wap to traverce through a string in reverce order
# string = 'srikanth'
# for item in range(len(string)-1, -1, -1):
#     print(string[item], end='')

#or
# for char in string[::-1]:
#     print(char, end='')

#or
# for item in reversed(string):
#     print(item, end='')

# 4. wap to count the number of characters present in the given string without using len function
# string = 'sri123kanth'
# count = 0
# for item in string:
#     count += 1
# print(count)

# 5. wap to print even index characters in the string
# string = 'srikanth'
# count = 0
# for item in range(0, len(string), 2):
#         print(string[item], end='')

#or
# for ele in string[::2]:
#     print(ele, end='')

# 6. wap to print the digit present inside string
# string = 'srikanth 1234 hi'
# for char in string:
#     if char.isdigit():
#         print(char, end="")

#or
# for char in string:
#     if '0'<=char<='9':
#         print(char)

# 7. wap to count the number of digit present in the string
# string = 'srikanth1234'
# count = 0
# for char in string:
#     if '0' <= char <= '9':
#         count+=1
# print(count)

# 8. wap to count the number of special character present in the string
# string = 'srikanth@.*1234'
# count = 0
# for char in string:
#     if not('0' <= char <= '9' or 'a' <= char <= 'z' or 'A' <= char <= 'Z'):
#         count += 1
# print(count)

# 9. wap to count the number of capital letter and small letter present in the string
# string = 'sriKAnth'
# upper = 0
# lower = 0
# for char in string:
#     if (char.islower()):
#         lower += 1
#     elif (char.isupper()):
#         upper += 1
#
# print('number of lower characters are', lower)
# print('number of upper characters are', upper)

# # or
# for char in string:
#     if 'a' <= char <= 'z':
#         lower += 1
# print(lower)

# 10. print tuple of char and its ascii avalue
# string = 'srikanth'
# for item in string:
#     print(item, ord(item))

# 11. wap to print the sum of all digit present in string
# s = 'sri123'
# sum = 0
# for i in s:
#     if i.isdigit():
#         sum += int(i)
# print(sum)

# 12. wap to print all the consonants present in the string and conunt of it
# s = 'srikanth*&'
# count = 0
# for i in s:
#     if i.isalpha():
#         if i not in 'aeiou':
#             count += 1
#             print(i, end='')
# print()
# print(count)


# 13. wap to print a tuple of index and its item in the string
# s = 'srikanth'
# for index, item in enumerate(s):
#     print((index, item))

# 14. wap to print a tuple of index and its item in the string without inbuilt Class
# s = 'srikanth'
# for i in range(len(s)):
#     print((i, s[i]))

# 15. wap to reverse a string atleast using 3 ways
# s = 'srikanth'
# for item in s[::-1]:
#     print(item)

# for item in range(len(s)-1, -1, -1):
#     print(s[item])

# for item in reversed (s):
#     print(item)

# 16. wap to extract only special char from string
# s = 'sri#$%123'
# for i in s:
#     if not ('a' <= i <= 'z' or 'A' <= i <= 'Z' or '0' <= i <= '9'):
#         print(i)

# 17. wap to check the if the given charracter present in string if it present return its index
# s = 'srikanth'
# char = 'm'
# for i in range(0, len(s)):
#     if char == s[i]:
#         print(i, 'is present at', s[i])

#or
# s = 'srikanth'
# char = 'm'
# for item in s:
#     if item == char:
#         print('is present at')
# else:
#     print('not present at')














