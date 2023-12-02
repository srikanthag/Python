# 1. wap to print the keys in a dictionary
# d = {'a' : 1, 'b' : 2, 'c': 3, 'd' : 4, 'e' : 5}

# traversing through the dictionary
# for key in d:
#     print(key)

#d.keys()
# for key in d:
#     d.key()
#     print(key)

#d.item()
# d = {'a' : 1, 'b' : 2, 'c': 3, 'd' : 4, 'e' : 5}
# for key, value in d.items():
#     print(value, end=',')

# 2. wap to print only the values form the dictionary
#d.values()
# for value in d:
#     d.values()
#     print(value)

#using dictionary key
# for key in d:
#     print(d[key])

#d.items()
# for key, value in d.items():
#     print(value)

#get methodj
# for key in d:
#     print(d.get(key))

# 3. wap to print the items in a dictionary along with the indexes
# d = {'a' : 1, 'b' : 2, 'c': 3, 'd' : 4, 'e' : 5}

#apply enumerate on dictionary variable
# for item, index in enumerate (d.items()):
#     print(item, index)

#enumerate(d.items())                            '''Deep unpacking'''
# d = {'a' : 1, 'b' : 2, 'c': 3, 'd' : 4, 'e' : 5}
# for index, (key, value) in enumerate (d.items()):
#     print(index, value, key)

# 4. wap to create a dictionary with the character and its count pair in a string
# string = "srikaainth"
# d = {}
# for char in string:
#     d[char] = string.count(char)
# print(d)

#using set(string)
# d = {}
# for char in set(string):
#     d[char] = string.count(char)
# print(d)

#without in-built method
# string = 'srikkant'
# d = {}
# for char in string:
#     count = 0
#     for j in string:
#         if char == j:
#             count += 1
#     d[char] = count
# print(d)

# defaultdict(): Defaultdict is a container like dictionaries present in the module collections. Defaultdict is a sub-Class of
# the dictionary Class that returns a dictionary-like object.
# from collections import defaultdict
# s = 'hello world'
# dd = defaultdict(int)
# for char in s:
#     if char in s:
#         dd[char] += 1
# print(dd)

# 5. wap to create a dictionary with word and its count pair
# s = 'hi how are you hi dude'
# d = {}
#counting
# list_ = s.split()
# for word in list_:
#     d[word] = list_.count(word)
# print(d)

#without using inbuilt method
# list_ = s.split()
# for word in list_:
#     if word not in d:
#         d[word] = 1
#     else:
#         d[word] += 1
# print(d)

# #using defaultdict method
# from collections import defaultdict
# s = 'hi how are you hi dude'
# dd = defaultdict(int)
# list_ = s.split()
#
# for word in list_:
#     dd[word] += 1
# print(dd)

# 6. wap to create a dictionary with word and its length pair
# s = 'hi how are you hi dude'
# d = {}
# list_ = s.split()
# for word in list_:
#     d[word] = len(word)
# print(d)

# 7. wap to create a dictionary with word and its length pair only if the word of even length
# s = 'hi dude how are you'
# d = {}
# list_ = s.split()
# for word in list_:
#     if len(word) % 2 == 0:
#         d[word] = len(word)
# print(d)

# 8. wap to create a dictionary with word and its length pair only if the word is starting with vowel
# s = 'hi dude how are you'
# d = {}
# list_ = s.split()
# for word in list_:
#     if word[0].lower() in 'aeiou':
#         d[word] = len(word)
# print(d)

# 9. wap to create a dictionary with word and its count only if the word not repeated
# s = 'hi dude hi how are how you'
# d = {}
# list_ = s.split()
# for word in list_:
#     if list_.count(word) == 1:
#         d[word] = list_.count(word)
# print(d)

# 10. wap to reverse the values in the dictionary if the value is of type string
# d = {'a': 'hello', 'b': 100, 'c': 10.2, 'd': 'world'}
# for key, value in d.items():
#     if isinstance(value, str):
#         d[key] =  value[::-1]
# print(d)

# 11. wap to get duplicate items and the number od times the repeated in the list
# names = ['apple', 'google', 'yahoo', 'gmail', 'apple', 'gmail', 'google']
# d = {}
# for name in names:
#     count = names.count(name)
#     if count > 1:
#         d[name] = count
# print(d)

# 12. wap to get the following output
# sentence = "hello world welcome to python programming hi there"
# op = {"h":["hello", "hi"], "w":["world", "welcome"], "t":["to", "there"], "p":["python", "programming"]}
# d= {}
# list_ = sentence.split()
# for word in list_:
#     if word[0] not in d:
#         d[word[0]] = [word]
#     else:
#         d[word[0]]+=[word]
# print(d)

#using defaultdict
# from collections import defaultdict
# dd = defaultdict(list)
# list_ = sentence.split()
# for word in list_:
#         dd[word[0]] += [word] #or# dd[word[0]].append(word)
# print(dd)

# 13. wap to create the dictionary with element and its index pair in the given list
# names = ['apple', 'google', 'yahoo', 'gmail', 'apple', 'gmail', 'google']
# d = {}
#normal dictionary
# for index, item in enumerate(names):
#     if item not in d:
#         d[item] = [index]
#     else:
#         d[item] += [index]
# print(d)

#using default dict
# names = ['apple', 'google', 'yahoo', 'gmail', 'apple', 'gmail', 'google']
# from collections import defaultdict
# dd = defaultdict(list)
# for index, item in enumerate(names):
#     dd[item] += [index]
# print(dd)

# 14. wap to flip key and values (swap case)
# d = {'a': 'hello', 'b': 100, 'c': 10.2, 'd': 'world'}
# d1 ={}
# for key in d:
#     value = d[key]
#     d1[value] = key
# print(d1)

# 15. wap to create a dictionary to count the number of occurrence of each char
# s = 'srikaanth'
# d = {}
# for char in s:
#     d[char] = s.count(char)
# print(d)

#or without inbuilt method
# d = {}
# for char in s:
#     if char not in d:
#         d[char] = 1
#     else:
#         d[char] += 1
# print(d)

# 16. wap to print the number if occurrence of character in a string without using inbuilt function
# s = 'srikanthtth'
# d = {}
# for char in s:
#     count = 0
#     for j in s:
#         if char == j:
#             count += 1
#     d[char] = count
# print(d)

# 17. wap to get the index of the each item in the bellow name
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail']
# d = {}
# for item, index in enumerate(names):
#     d[item] = index
# print(d)

# 18. grouping file with same extension
# files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'youtube.com']
# d = {}
# for item in files:
#     l = item.split('.')
#     d[l[0]] = l[1]
# print(d)

# 19. program to create a dictionary with only the repeated character and count of the same
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail']
# d = {}
# for item in names:
#     if names.count(item) > 1:
#         d[item] = names.count(item)
# print(d)



# 20. wap to get alll the duplicate item and the number of times the items is repeated in the list
# names = ['apple', 'google', 'apple', 'yahoo', 'facebook', 'gmail', 'google']
# d = {}
# for item in names:
#     if names.count(item) > 1:
#         d[item] = names.count(item)
# print(d)

# 21. grouping flowers and animals in the list
# from collections import defaultdict
# dd = defaultdict(list)
# items = ['lotus-flower', 'cat-animal', 'rose-flower', 'dog-animal']
# for item in items:
#     l = item.split('-')
#     dd[l[1]] = [l][0]
# print(dd)

# 22. grouping even and odd number
# numbers = [1,2,3,4,5,6,7,8,9]
# l = []
# l1 = []
# for item in numbers:
#     if item % 2 ==0:
#         l.append(item)
#     else:
#         l1.append(item)
# print(l)
# print(l1)

# 23. creating dictionary city and population using Comprehension
# city = ['bangalore', 'mangalore', 'mysore', 'chikkaballapura']
# pop = [100, 200, 300]
# d = {}
# for item in range(len(city)):
#     d[city[item]] = pop[item]
# print(d)
#
# z = zip(city, pop)
# print(dict(z))
#
# dic = {city[item]: pop[item] for item in range(len(city))}
# print(dic)
