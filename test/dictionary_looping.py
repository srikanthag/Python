#wap to print the number if occurance of character in a string without using inbuild function
# s = 'srikanthtth'
# d = {}
# for char in s:
#     count = 0
#     for j in s:
#         if char == j:
#             count += 1
#     d[char] = count
# print(d)

#wap to get the index of the each item in the bellow name
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail']
# d = {}
# for item, index in enumerate(names):
#     d[item] = index
# print(d)

#grouping file with same extension
# files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'youtube.com']
# d = {}
# for item in files:
#     l = item.split('.')
#     d[l[0]] = l[1]
# print(d)

#program to create a dictionary with only the repeated character and count of the same
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail']
# d = {}
# for item in names:
#     if names.count(item) > 1:
#         d[item] = names.count(item)
# print(d)



# wap to get alll the duplicate item and the number of times the items is repeated in the list
# names = ['apple', 'google', 'apple', 'yahoo', 'facebook', 'gmail', 'google']
# d = {}
# for item in names:
#     if names.count(item) > 1:
#         d[item] = names.count(item)
# print(d)

#grouping flowers and animals in the list
# from collections import defaultdict
# dd = defaultdict(list)
# items = ['lotus-flower', 'cat-animal', 'rose-flower', 'dog-animal']
# for item in items:
#     l = item.split('-')
#     dd[l[1]] = [l][0]
# print(dd)

#grouping even and odd number
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

#creating dictionary city and population using Comprehension
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



#wap to flip key and value
