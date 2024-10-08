# 1. wap to create a dictionary with item and its index pair
s = 'hello'
dict_ = {item: index for index, item in enumerate(s)}
print(dict_)

# 2. wap to create a dictionary with word and its length pair
s = 'hi how are you'
s1 = s.split(' ')
dict_ = {word: len(word) for word in s1}
print(dict_)

# 3. wap to create a dictionary with character, and it counts pair
s = 'srikanthyuuuag'
dict_ = {char: s.count(char) for char in s}
print(dict_)

# 4. wap to create dictionary of word and its count
string = 'hi hi hi how are you'
s1 = string.split(' ')
dict_ = {word: s1.count(word) for word in s1}
print(dict_)

# 5. wap to create a dictionary of word and its count pair only if the word is even length
s = 'hi howe are you'
s1 = s.split(' ')
dict_ = {word: s1.count(word) for word in s1 if len(word) % 2 == 0}
print(dict_)

# 6. wap to create a dictionary with index and word pair if the word is of odd length reverse it else kept it as is
s1 = 'hi dude how are yuo'
d = {}
s = s1.split(' ')
dict_ = {index: item if len(item) % 2 == 0 else item[::-1] for index, item in enumerate(s)}
print(dict_)

# 7. wap to create a dictionary with word and its length pair only if the word starting with vowels
s1 = 'hi how are uou'
s = s1.split(' ')
dict_ = {word: len(word) for word in s if word[0] in 'aeiouAEIOU'}
print(dict_)

# 8. wap to create a dictionary of item and its index pair if the item is of string data type reverse it or else keep is as it
list_ = ['sri', 10, 10.2, True, 'kanth']
dict_ = {index: item[::-1] if isinstance(item, str) else item for index, item in enumerate(list_)}
print(dict_)

# 9. wap to create a dictionary with index and word pair if word is of type string keep it as it is else reverse it
list_ = ['sri', 10, 10.2, True, 'kanth']
dict_ = {index: item if isinstance(item, str) else str(item)[::-1] for index, item in enumerate(list_)}
print(dict_)

# 10. wa comprehension to flip or swap keys and values in a dictionary
d = {1:'a', 2:'b', 3:'c'}
dict_ = {d[item]: item for item in d}
print(dict_)

# 11. wap to create a dictionary of character and its ascii value pairs
s = 'hello'
dict_ = {item: ord(item) for item in s}
print(dict_)
