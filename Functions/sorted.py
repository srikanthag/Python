#default sorting the collection datatype
# s = 'srikanth'
# print(sorted(s))

# l = [5,7,4,6,9,3]
# print(sorted(l))

# l = ['hi', 'python', 'how']
# print(sorted(l))

# t = ('python', 'java', 'ruby')
# print(sorted(t))
# print(sorted(t, reverse=true))

# set_ = {'hi', 'python', 'how'}
# print(sorted(set_))

# d = {'hi': 5, 'python': 6, 'how': 3}
# print(sorted(d.items()))

#custome sorting

# t = ('python', 'java', 'ruby')
# print(sorted(t, key=len))

#wap to sort the element present in the list based on their length
# l = ['python', 'java', 'ruby']
# print(sorted(l, key=len))             #ascending order

# l = ['python', 'java', 'ruby']
# print(sorted(l, key=len, reverse=True))         #descending order

#wap to find the longest  and shortest word in the following string
# s = "hi how are you srikanth"
# s1 = s.split()
# shortest, *rest, longest = sorted(s1, key=len)
# print(shortest)
# print(longest)

#wap to print longest and shortest words along with their lengths in the below sentance
# s = "hi how are you srikanth"
# s1 = s.split()
# shortest, *rest, longest = sorted(s1, key=len)
# print((shortest, len(shortest)), (longest, len(longest)))

#wap to sort the below list elements based on last element of each element
# l = ['python', 'java', 'ruby']
#using def
# def last_(ele):
#     return ele[-1]
# print(sorted(l, key=last_))

#using lambda
# print(sorted(l, key=lambda item:item[-1]))

#wap to sort the below list based on first char of each element
# l = ['python', 'java', 'ruby']
# print(sorted(l))

#wap to sort the below list based on middle char of each element
# l = ['pytahon', 'jva', 'ruby']
# print(sorted(l, key=lambda item: len(item) // 2 == 0))

#sorting dictionary
#sorting a dictionary based on key
# d = {'hi': 5, 'python': 6, 'how': 3}

#based on ASCII value
# print(sorted(d))
# print(sorted(d.keys()))
# print(sorted(d.items()))

#based on length
# d = {'hi': 5, 'python': 6, 'how': 3}
# print(sorted(d, key=len))
# print(sorted(d.keys(), key=len))
# print(dict(sorted(d.items(), key=lambda item: len(item[0]))))   #sort a dictinary both key and value

#wap to sort the dictionary based on keys last item
# d = {'hi': 5, 'how': 3, 'python': 6}
# print(dict(sorted(d.items(), key=lambda item: item[0][-1])))

#wap to sort a dictionary based on values
# d = {'hi': 5, 'how': 3, 'python': 6}
# print(sorted(d.values()))
# print(dict(sorted(d.items(), key=lambda item: item[-1])))

#wap to sort the above list based on the temperature  #confuse
# temperatures = [('delhi', 32), ('mumbi', 27), ('kolkata, 30'), ('chenni', 35)]
# print(sorted(temperatures, key=lambda item: item[-1]))

#wap to get most repeated word
# sentance = 'hi hi how are you you'
# s = sentance.split()
# d_count = {word: s.count(word) for word in s}
# res=sorted(d_count.items(), key=lambda item: item[-1])
# print(res[-1])

#wap oto print the longest word with its length

# sentance = 'hi hi howfdd are you you'
# s = sentance.split()
# d_len = {word: len(word) for word in s}
# res = sorted(d_len, key=lambda item: len(item))
# print(res[-1], len(res[-1]))

#wap longest non repeated word
# sentance = 'hi python python langiage programming programming hi howfdd are you you'
# s = sentance.split()
# d = {item: len(item) for item in s if s.count(item)==1}
# res = sorted(d.items(), key=lambda item: item[-1])
# print(res[-1])

#wap sort based on the names, class, age
# l = [{'name': 'Ram', 'class': 6, 'age': 12 },
#     {'name': 'Sham', 'class': 12, 'age': 18 },
#     {'name': 'John', 'class': 8, 'age': 13 } ]

# print(sorted(l, key=lambda item: item['class']))
# print(sorted(l, key=lambda item: item['age']))
# print(sorted(l, key=lambda item: item['name']))

















