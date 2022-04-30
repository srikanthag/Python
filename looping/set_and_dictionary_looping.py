# sets
# wap to traverse through set and print each element
# s = {'python', 'dad', 'hi'}
# for item in s:
#     print(item)

# wap to print the elements in the sets reversed order
# not possible

# wap to remove the given element from the set
# s = {'python', 'dad', 'hi'}
# s.discard('hi')
# print(s)

# wap to create a set with the elements in the list if the elemnt is paliandrome
# l = ['python', 'dad', 'hi', 'malayalam', 'java', 'mom']
# s = set()
# for item in l:
#     if item == item[::-1]:
#         s.add(item)
# print(s)


#Dictionary

#wap to print the keys in a dictionary
# d = {'a' : 1, 'b' : 2, 'c': 3, 'd' : 4, 'e' : 5}
#traversing through the directli
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

#wap to print only the values form the dictionary
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

#get method
# for key in d:
#     print(d.get(key))


#wap to print the items in a dictionary along with the indecies
# d = {'a' : 1, 'b' : 2, 'c': 3, 'd' : 4, 'e' : 5}
#apply enumerate on dictionary variable
# for item, index in enumerate (d.items()):
#     print(item, index)

#enumerate(d.items())                            '''Deep unpacking'''
# d = {'a' : 1, 'b' : 2, 'c': 3, 'd' : 4, 'e' : 5}
# for index, (key, value) in enumerate (d.items()):
#     print(index, value, key)

#wap to create a dictionary with the character and its count pair in a string
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

#defaultdict()
# from collections import defaultdict
# s = 'hello world'
# dd = defaultdict(int)
# for char in s:
#     if char in s:
#         dd[char] += 1
# print(dd)

#wap to create a dictionary with word and its count pair
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

#using defaultdict method
# from collections import defaultdict
# s = 'hi how are you hi dude'
# dd = defaultdict(int)
# list_ = s.split()
#
# for word in list_:
#     dd[word] += 1
# print(dd)

#wap to create a dictionary with word and its length pair
# s = 'hi how are you hi dude'
# d = {}
# list_ = s.split()
# for word in list_:
#     d[word] = len(word)
# print(d)

#wap to create a dictionary with word and its length pair only if the word of even length
# s = 'hi dude how are you'
# d = {}
# list_ = s.split()
# for word in list_:
#     if len(word) % 2 == 0:
#         d[word] = len(word)
# print(d)

#wap to create a dictionary with word and its length pair only if the word is starting with vowel
# s = 'hi dude how are you'
# d = {}
# list_ = s.split()
# for word in list_:
#     if word[0].lower() in 'aeiou':
#         d[word] = len(word)
# print(d)

#wap to create a dictionary with word and its count only if the word not repeated
# s = 'hi dude hi how are how you'
# d = {}
# list_ = s.split()
# for word in list_:
#     if list_.count(word) == 1:
#         d[word] = list_.count(word)
# print(d)

#wap to reverse the values in the dictionary if the value is of type string
# d = {'a': 'hello', 'b': 100, 'c': 10.2, 'd': 'world'}
# for key, value in d.items():
#     if isinstance(value, str):
#         d[key] =  value[::-1]
# print(d)

#wap to get duplicate items and the number od times the repeated in the list
# names = ['apple', 'google', 'yahoo', 'gamil', 'apple', 'gmail', 'google']
# d = {}
# for name in names:
#     count = names.count(name)
#     if count > 1:
#         d[name] = count
# print(d)

#wap to get the following output
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

#wap to create the dictionary with element and its index pair in the given list
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

#wap to flip key and values (swap case)
# d = {'a': 'hello', 'b': 100, 'c': 10.2, 'd': 'world'}
# d1 ={}
# for key in d:
#     value = d[key]
#     d1[value] = key
# print(d1)

#wap to create a dictionary to count the no of occurance of each char
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
