#wap to print 'Bangalore' 10 times without using for and while loop
# a = 'bangalore'
# print(a\n * 10)

#wap to count the number of digit and alphabets in the string
# string = '1234python23'
# digit = 0
# alphabet = 0
# for item in string:
#     if item.isalpha():
#         alphabet += 1
#     elif item.isdigit():
#         digit += 1
# print(alphabet)
# print(digit)

#wap to create a string by swapping the cases of the character without using inbuilt method
# string = 'SRIkanth'
# res = ''
# for item in string:
#     if 'a' <= item <= 'z':
#         res += chr(ord(item) - 32)
#     elif 'A' <= item <= 'Z':
#         res += chr(ord(item) + 32)
#     else:
#         res += item
# print((res))

#wap to create a string with only consonets present in the string
# string = 'Python selenium'
# st = ''
# for item in string:
#     if item not in 'aeiouAEIOU':
#         st += item
# print(st)


#wap to search for a character in the string and returns its first occurance position
# s = 'srikanith'
# char = 'i'
# print(s.find('i'))
#
# #or
# for item in s:
#     if char == item:
#         ind = s.index(char)
#         print('characeter present at ', ind)
#
# #range
# for index in range(len(s)):
#     if char == s[index]:
#         print('characeter present at ', index)
#         break
#
# #enumereate
# for index, item in enumerate(s):
#     print(char, index)
#     break

#wap to print the character and its ascii value if the character is a vowel in the string
# string = 'she sells sea shells on the sea shores'
# for item in string:
#     if item in 'aeiouAEIOU':
#         print(item, ord(item))


#wap to print word and its length in the string
# string = 'she sells sea shells on the sea shores'
# s = string.split(' ')
# for item in s:
#     print(item, len(item))


#wap to print the words that are string with vowels in the string
# string = 'she is a very good actor'
# s = string.split(' ')
# for item in s:
#     if item[0] in 'AEIOUaeiou':
#         print(item)

#wap to count the number of character in the string without using inbuilt function
# string = 'hello worls'
# count = 0
# for item in string:
#     count += 1
# print(count)


#wap to reverse a string without using slicing
# string = 'hello worls'
# for item in reversed(string):
#     print(item)

# for item in range(len(string)-1, -1, -1):
#     print(string[item])

#using concatination
# s = ''
# for char in string:
#     s = char + s
# print(s)