#wap to create a list of squre for element in list
# l= [1,2,3,4]
# #normal method
# res = []
# for i in l:
#     res.append(i**2)
# print(res)

#comprehension method
# l= [1,2,3,4]
# res = [i ** 2 for i in l]
# print(res)

# l = [1,2,3]
# op = [item ** 2 for item in l]
# print(op)

#wap to create a list of tuples which is having index and curresponding item
# l = [1, 2, 3]
# # l_index = []
#normal
# for item, index in enumerate(l):
#     l_index.append((index, item))
# print(l_index)

#comprenhension
# l_index = [item for item in enumerate(l)]
# print(l_index)

#or
# l_index = [(item, index) for index, item in enumerate(l)]
# print(l_index)

#wap to create a list of even numbers from the below list
# l = [1,2,3,4,5,6,7,8]
# l1 = []
# #normal
# for i in l:
#     if i % 2 == 0:
#         l1.append(i)
# print(l1)

#comprehension
# even = [item for item in l if item % 2 == 0]
# print(even)

#create 2 list even and odd
# l = [1,2,3,4,5,6,7,8]
#normal methof
# even = []
# odd = []
# for i in l:
#     if i % 2 ==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

#comprehension
# even = [item for item in l if item % 2 == 0]
# odd = [item for item in l if item % 2 != 0]
# print(even)
# print(odd)

#wap to create a list using the following list if the word is of even length store the word as it is if it odd length
#reverse the word and store it
# l = ['python', 'node js', 'selenium', 'javea2']
# l1 = []

#normal
# for i in l:
#     if len(i) % 2 ==0:
#         l1.append(i)
#     else:
#         l1.append(i[::-1])
# print(l1)

#comprehension
# l1 = [item if len(item) % 2 == 0 else item[::-1] for item in l]
# print(l1)

#wap to create a list from the list if elements are type string keep the as it is else reverse it
# l = ['python', 'node js', 10, 12.4, True, 'selenium', 'javea2']
#
# #normal
# l1 = []
# for item in l:
#     if not isinstance(item, str):
#         l1.append(str(item)[::-1])
#     else:
#         l1.append(item)
# print(l1)

#comprehension
# l1 = [str(item)[::-1] if not isinstance(item, str) else item for item in l]
# print(l1)

#wa list comprehension to create a list with strating with vowels
# l = ['python', 'node js', 'english', 'selenium', 'javea2']
#
# l1 = [item for item in l if item[0] in 'aeiouAEIOU']
# print(l1)

# wap to print integers present in the list
# l = ['python', 10, 3.2, 'selenium', 'java']
# l1 = [item for item in l if isinstance(item, int)]
# print(l1)

#print all numeric datatypes by using isinstance
# l = ['python', 10, 3.2, 'selenium', 1+5j, True, 'java']
# l1 = [item for item in l if isinstance(item, (int, float, complex))]
# print(l1)

##wap to print length of each string in the list
# l = ['python', 'selenium', 'java']
# l1 = [len(item) for item in l]
# print(l1)

#wap to print the strings which are of even length in the list
# l = ['python', 'selenium', 'True', 'java', 'sri', 'for']
# l1 = [item for item in l if len(item) % 2 == 0]
# print(l1)

#wap to print the strings which are of odd length in the list
# l = ['python', 'selenium', 'True', 'java', 'sri', 'for']
# l1 = [item for item in l if len(item) % 2 != 0]
# print(l1)

# wap to print the elements in the list if the element is of even length print as it is, if it is odd then
# reverse and print
# l = ['python', 'selenium', 'True', 'java', 'sri', 'for']
# l1 = [item if len(item) % 2 == 0 else item[::-1] for item in l]
# print(l1)

#wap to reverse the elements inside the list if the elements of type string or else keep it as it is
# l = ['python', 10, 2.2, True, 'selenium', 'True', 'java', 'sri', 'for']
# l1 = [item[::-1] if isinstance(item, str) else item for item in l]
# print(l1)

#wap to print the element which have starting with vowel
# l = ["Amezon", "Flipcart", "walmart", "gmail", "yahoo"]
# l1 = [item for item in l if item[0] in 'aeiouAEIOU']
# print(l1)

#wap print all the extensions in the followig list
# l = ['youtube.txt', 'amazon.pdf', 'apple.xls', 'flipcart.in']
# l1 = [(item.split('.')[1]) for item in l]
# print(l1)

#wap print all the file name in the followig list
# l = ['youtube.txt', 'amazon.pdf', 'apple.xls', 'flipcart.in']
# l1 = [(item.split('.')[0]) for item in l]
# print(l1)

#wap to print the file name if the file name is of odd length                        ###confuse
# files = ['youtube.txt', 'amazon.pdf', 'apple.xls', 'flipcart.in']
# l1 = [item if len(item) % 2 == 0 else item for item in files]
# print(l1)

#wap to return index of the first occurance of the given element
# number = [10, 20, 30, 40, 50, 80, 40, 30, 80]
# num = 80
# l1 = [item for item, index in enumerate(number) if index == num]
# print(l1)