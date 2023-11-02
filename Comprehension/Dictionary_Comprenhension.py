#wap to create a dictionary with item and its index pair
# s = 'hello'
# d = {}
#normal
# for index, item in enumerate(s):
#     d[item] = index
# print(d)

#comprenhision
# dict_ = {item: index for index, item in enumerate(s)}
# print(dict_)


# wap to create a dictionary with word and its length pair
# s = 'hi how are you'
#normal
# d = {}
# s1 = s.split(' ')
# for word in s1:
#     d[word] = len(word)
# print(d)

#comprension
# dict_ = {word: len(word) for word in s1}
# print(dict_)

#wap to create a dictionary with character and it count pair
# s = 'srikanthyuuuag'
#normal
# d = {}
# for char in s:
#     d[char] = s.count(char)
# print(d)

#comprenhision
# dict_ = {char: s.count(char) for char in s}
# print(dict_)

#wap to create dictionary of word and its count
# string = 'hi hi hi how are you'
# s1 = string.split(' ')
# #normal
# d = {}
# s = string.split(' ')
# for word in s:
#     d[word] = s.count(word)
# print(d)

#comprenhension
# dict_ = {word: s1.count(word) for word in s1}
# print(dict_)


#wap to create a dictionary of word and its count pair only if the word is even length
# s = 'hi howe are you'
#normal
# d = {}
# s1 = s.split(' ')
# for word in s1:
#     if len(word) % 2 == 0:
#         d[word] = s.count(word)
# print(d)

#comprenhision
# dict_ = {word: s1.count(word) for word in s1 if len(word) % 2 == 0}
# print(dict_)

#wap to create a dictionary with index and word pair if the word is of odd length reverse it else keept it as is
# s1 = 'hi dude how are yuoo'
# d = {}
# s = s1.split(' ')
# for index, item in enumerate(s):
#     if len(item) % 2 == 0:
#         d[index] = item
#     else:
#         d[index] = item[::-1]
# print(d)
#
# comprensionsdf
# dict_ = {index: item if len(item) % 2 == 0 else item[::-1] for index, item in enumerate(s)}
# print(dict_)


#wap to create a dictionary with word and its length pair only if the word starting with vowels
# s1 = 'hi how are uou'
# s = s1.split(' ')
#comp
# dict_ = {word: len(word) for word in s if word[0] in 'aeiouAEIOU'}
# print(dict_)

#wap to create a dictionary of item and its index pair if the item is of string data type reverse it or else keet is as it
# list_ = ['sri', 10, 10.2, True, 'kanth']
# dict_ = {index: item[::-1] if isinstance(item, str) else item for index, item in enumerate(list_)}
# print(dict_)

#wap to create a dictionary with index and word pair if word is of type string keep it as it is else reverse it
# list_ = ['sri', 10, 10.2, True, 'kanth']
# dict_ = {index: item if isinstance(item, str) else str(item)[::-1] for index, item in enumerate(list_)}
# print(dict_)

#wa comprension to flip or swap keys and values in a dictionary
# d = {1:'a', 2:'b', 3:'c'}
# dict_ = {d[item]: item for item in d}
# print(dict_)

#wap to create a dictionary of character and its ascii value pairs
# s = 'hello'
# dict_ = {item: ord(item) for item in s}
# print(dict_)

