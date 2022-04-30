#wap to remove the all the duplicate elements in the list
# names = ['apple', 'google', 'google', 'apple', 'yahoo', 'google']
# s = set()
# for item in names:
#     s.add(item)
# print(s)

#or
# res = []
# for item in names:
#     if item not in res:
#         res.append(item)
# print(res)

#wap to print all numeric value in list
# item = ['apple', 1.2, 'google', '12.6', 26, '100']
# for num in item:
#     if isinstance(num,(int, float, complex)):
#         print(num, end=',')



#wap wap to to sum of all even number in the given string
# l = "hello 123 world 567 welcome to 9724 python"
# even = 0
# for char in l:
#     if l.isdigit():
#         if int(char) % 2 == 0:
#             even += int(char)
# print(even)

#wap to create a set with all the language which starts with 'P'
# language = ['Python', 'java', 'Perl', 'PHP', 'Ruby']
# s = set()
# for item in language:
#     if item[0] in 'P':
#         set.add(item)
# print(set)

#build a list with only even length string
# names = ['apple', 'google', 'yahoo', 'facebook', 'yelp']
# l = []
# for item in names:
#     if len(item) % 2 == 0:
#         l.append(item)
# print(l)

#reverse the item of list of odd length otherwise keep its as is
# names = ['apple', 'google', 'yahoo', 'facebook', 'yelp']
# l = []
# for item in names:
#     if len(item) % 2 == 0:
#         l.append(item)
#     else:
#         l.append(item[::-1])
# print(l)

#wap to print the sum of entire list and sum if only internal list
# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# entire_sum = 0
# for item in l:
#     internal_sum = 0
#     for i in item:
#         internal_sum += i
#         entire_sum += i
#     print(internal_sum)
# print(entire_sum)

#list of prime numbers
# prime_ = []
# for n in range (1, 100):
#     if n > 1:
#         for i in range (2, n):
#             if n % i == 0:
#                 break
#         else:
#             prime_.append(n)
# print(prime_)

#wap to reverse the list as below
# words = ['hi', 'hello', 'python']
# l = []
# for item in words[::-1]:
#     l.append(item[::-1])
# print(l)

#wap rotate items of the list
# language = ['Python', 'java', 'Perl', 'PHP', 'Ruby']
# k = 3
# for i in range(k):
#     item = language.pop()
#     language.insert(0,item)
# print(language)