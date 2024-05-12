# 1. wap to create a list of square for element in list
l= [1,2,3,4]
res = [i ** 2 for i in l]
print(res)

# 2. wap to create a list of tuples which is having index and corresponding item
l = [1, 2, 3]
l_index = [item for item in enumerate(l)]
print(l_index)

# Alternate
l_index = [(item, index) for index, item in enumerate(l)]
print(l_index)

# 3. wap to create a list of even numbers from the below list
l = [1,2,3,4,5,6,7,8]
even = [item for item in l if item % 2 == 0]
print(even)

# 4. create 2 list even and odd
l = [1,2,3,4,5,6,7,8]
even = [item for item in l if item % 2 == 0]
odd = [item for item in l if item % 2 != 0]
print(even)
print(odd)

# 5. wap to create a list using the following list if the word is of even length store the word as it is if it odd length reverse the word and store it
l = ['python', 'node js', 'selenium', 'javea2']
l1 = [item if len(item) % 2 == 0 else item[::-1] for item in l]
print(l1)

# 6. wap to create a list from the list if elements are type string keep the as it is else reverse it
l = ['python', 'node js', 10, 12.4, True, 'selenium', 'javea2']
l1 = [str(item)[::-1] if not isinstance(item, str) else item for item in l]
print(l1)

# 7. wa list Comprehension to create a list with starting with vowels
l = ['python', 'node js', 'english', 'selenium', 'javea2']
l1 = [item for item in l if item[0] in 'aeiouAEIOU']
print(l1)

# 8. wap to print integers present in the list
l = ['python', 10, 3.2, 'selenium', 'java']
l1 = [item for item in l if isinstance(item, int)]
print(l1)

# 9. print all numeric datatypes by using isinstance
l = ['python', 10, 3.2, 'selenium', 1+5j, True, 'java']
l1 = [item for item in l if isinstance(item, (int, float, complex))]
print(l1)

# 10. wap to print length of each string in the list
l = ['python', 'selenium', 'java']
l1 = [len(item) for item in l]
print(l1)

# 11. wap to print the strings which are of even length in the list
l = ['python', 'selenium', 'True', 'java', 'sri', 'for']
l1 = [item for item in l if len(item) % 2 == 0]
print(l1)

# 12. wap to print the strings which are of odd length in the list
l = ['python', 'selenium', 'True', 'java', 'sri', 'for']
l1 = [item for item in l if len(item) % 2 != 0]
print(l1)

# 13. wap to print the elements in the list if the element is of even length print as it is, if it is odd then reverse and print
l = ['python', 'selenium', 'True', 'java', 'sri', 'for']
l1 = [item if len(item) % 2 == 0 else item[::-1] for item in l]
print(l1)

# 14. wap to reverse the elements inside the list if the elements of type string or else keep it as it is
l = ['python', 10, 2.2, True, 'selenium', 'True', 'java', 'sri', 'for']
l1 = [item[::-1] if isinstance(item, str) else item for item in l]
print(l1)

# 15. wap to print the element which have starting with vowel
l = ["Amezon", "Flipcart", "walmart", "gmail", "yahoo"]
l1 = [item for item in l if item[0] in 'aeiouAEIOU']
print(l1)

# 16. wap print all the extensions in the followig list
l = ['youtube.txt', 'amazon.pdf', 'apple.xls', 'flipcart.in']
l1 = [(item.split('.')[1]) for item in l]
print(l1)

# 17. wap print all the file name in the followig list
l = ['youtube.txt', 'amazon.pdf', 'apple.xls', 'flipcart.in']
l1 = [(item.split('.')[0]) for item in l]
print(l1)

# 18. wap to print the file name if the file name is of odd length
files = ['youtube.txt', 'amazon.pdf', 'apple.xls', 'flipcart.in']
l1 = [(item.split('.')[0]) for item in files if len(item) % 2 == 1]
print(l1)

# 19. wap to return index of the first occurrence of the given element
number = [10, 20, 30, 40, 50, 80, 40, 30, 80]
num = 80
l1 = [item for item, index in enumerate(number) if index == num]
print(l1)
