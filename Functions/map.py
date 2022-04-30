# map() map applies a function to all item in the input list
# l = ['hi', 'mom']
# pali = lambda string: 'paliondrom' if string == string[::-1] else 'not paliondrome'
# res = map(pali, l)
# print(list(res))

#wap that checks if given list of numbers are even or not
# l = [1,2,3,4,5]
# even_odd = lambda n: 'it is even' if n % 2 == 0 else 'it is odd'
# res = map(even_odd, l)
# print(list(res))

#wap to return the string which are starating with vowels
# l = ['apple', 'gmail', 'yahoo', 'flipkart']
# def vovel(char):
#     if char[0] in 'aeiouAEIOU':
#         return char
# res =map(vovel, l)
# print(list(res))

#wap to convert all the strings in the list to upper case using map
# s = 'hi how are you'
# sen = s.split()
# def upper_(wor):
#     return wor.upper()
# r = map(upper_, sen)
# print(list(r))

#or
# wor = lambda item:item.upper()
# res = map(wor, s.split())
# print(list(res))



#wap to convert all the elements in the list to upper case using map
# l = ['apple', 'GMAIL', 'yahoo', 'flicpcart']
# def upper(char):
#         return char.upper()
# res = map(upper, l)
# print(list(res))


#wap to convert all negative numbers in the list to positive ######
# l = [-1, -2, -3]
# def neg(num):
#     return abs(num)
# res = map(neg, l)
# print(list(res))


# s = lambda item: abs(item)
# # print(s)
# res = map(s, l)
# print(list(res))


#wap that returns the list of numbers raised to the power of their indeces using maps
# l = [10, 20, 30, 40]
# def index_(item):
#     return item[1] ** item[0]

# res = map(index_, enumerate(l))
# print(list(res))


#wap that returns all the words in lower case in the given sentance
# l = ['APPLE', 'GMAIL', 'YAHOO', 'FLOPCART']
# # def lower(char):
# #         return char.lower()
# # res = map(lower, l)
# # print(list(res))

# s = lambda item: item.lower()
# res = map(s,l)
# print(list(res))


#wap to get list of lens of each word
# s = 'hi how are yoy'
# l = s.split()
# res = map(len, l)
# print(list(res))

# ss = lambda item: len(item)
# res = map(ss, l)
# print(list(res))

#or
# def word_len(word):
#     return word, len(word)
# res = map(word_len, l)
# print(list(res))

#wap to get list of tuples character and ascii value pair
# s = 'srikanth'

# def char_asci(char):
#     return char, ord(char)
# res = map(char_asci, s)
# print(list(res))

#wap at add the following list elements simaeltaneously
# a = [1,2,3,4]
# b = [5,6,7,8]
# def add_(item1, item2):
#     return item1 + item2
#
# res = map(add_, a, b)
# print(list(res))


# l = ['sri', 'raj']
# def indi(word):
#     return word
#
# res = list(map(list, l))
# print(res)

#squre of each element inside the list
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def sqr(item):
#     return item ** 2
#
# res = map(sqr, l)
# print(list(res))

# sq = lambda item: item ** 2
# res = map(sq,l)
# print(list(res))
