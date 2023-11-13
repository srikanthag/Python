# 1. wag for simple function

# def greet():
#     yield 'hi'
#     yield 'how'
#
# msg = greet()
# print(msg)
#
# for item in msg:
#     print(item)


# 2. wag to return square number
# def squares(l):
#     for item in l:
#         yield item**2
#
# l = [1,2,3,4]
# res = (item ** 2 for item in l)
# print(res)  #address
# print(list(res))
# print(dir(res))     #both iter and next method

# print(next(res))
# print(next(res))
# print(next(res))

# 3. wa generator expression to yield even numbers in the range 1 -50
# def even():
#     for item in range(51):
#         if item % 2 == 0:
#             yield item
# print(even())
# print(list(even()))

# 4. wag fuction and expression to yield tha names starting with vowels
# names = ['john', 'srikanth', 'evagreen', 'anabella']
# def vow(names):
#     for item in names:
#         if item[0] in 'AEIOUaeiou':
#             yield item
#
# vowel = vow(names)
# print(vowel)
# print(list(vowel))

# vow_ = (item for item in names if item[0] in 'AEIOUaeiou')
# print(vow_)
# print(list(vow_))

# 5. wag function expression to yield length of each line in file only if the line is not empty
# path = r"C:\Users\srikanth\PycharmProjects\python_new\File_Directory\Text_File_Sample\sample.txt"
# def len_file():
#     with open(path) as file:
#         for line in file:
#             if line.strip():
#                 yield line
# lines = print(len_file)
# print(lines)
#
# len = (len(line) for line in file if line.strip())
# print(len)
# print(list(len))
