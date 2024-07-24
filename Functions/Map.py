# 1. waf that checks if given list of items are palindrome or not
l = ['hi', 'mom']
pali = lambda string: 'palindrome' if string == string[::-1] else 'not palindrome'
res = map(pali, l)
print(list(res))

# 2. waf that checks if given list of numbers are even or not
l = [1,2,3,4,5]
even_odd = lambda n: 'it is even' if n % 2 == 0 else 'it is odd'
res = map(even_odd, l)
print(list(res))

# 3. waf to return the string which are starting with vowels
l = ['apple', 'gmail', 'yahoo', 'flipkart']
def vowel(char):
    if char[0] in 'aeiouAEIOU':
        return char
res =map(vowel, l)
print(list(res))

# Alternative
v = lambda item:'vowel' if item[0] in 'aeiouAEIOU' else 'consonants'
res = map(v,l)
print(list(res))

# 4. waf to convert all the strings in the list to upper case using map
s = 'hi how are you'
sen = s.split()
def upper_(wor):
    return wor.upper()
r = map(upper_, sen)
print(list(r))

# Alternative
wor = lambda item:item.upper()
res = map(wor, s.split())
print(list(res))

# 5. waf to convert all the elements in the list to upper case using map
l = ['apple', 'GMAIL', 'yahoo', 'flicpcart']
def upper(char):
        return char.upper()
res = map(upper, l)
print(list(res))

# 6. waf to convert all negative numbers in the list to positive
l = [-1, -2, -3]
def neg(num):
    return abs(num)
res = map(neg, l)
print(list(res))

# Alternative
s = lambda item: abs(item)
# print(s)
res = map(s, l)
print(list(res))

# 7. waf that returns the list of numbers raised to the power of their indexes using maps
l = [10, 20, 30, 40]
def index_(item):
    return item[1] ** item[0]

res = map(index_, enumerate(l))
print(list(res))

# 8. waf that returns all the words in lower case in the given sentance
l = ['APPLE', 'GMAIL', 'YAHOO', 'FLOPCART']
s = lambda item: item.lower()
res = map(s,l)
print(list(res))

# 9. wap to get list of lens of each word
s = 'hi how are yoy'
l = s.split()
res = map(len, l)
print(list(res))

ss = lambda item: len(item)
res = map(ss, l)
print(list(res))

# Alternative
def word_len(word):
    return word, len(word)
res = map(word_len, l)
print(list(res))

# 10. wap to get list of tuples character and ascii value pair
s = 'srikanth'
def char_asci(char):
    return char, ord(char)
res = map(char_asci, s)
print(list(res))

# 11. wap at add the following list elements simultaneously
# a = [1,2,3,4]
# b = [5,6,7,8]
# def add_(item1, item2):
#     return item1 + item2
#
# res = map(add_, a, b)
# print(list(res))


# l = ['sri', 'raj']
# def indi(word):
#     return word
#
# res = list(map(list, l))
# print(res)

# 12. square of each element inside the list
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def sqr(item):
#     return item ** 2
#
# res = map(sqr, l)
# print(list(res))

# sq = lambda item: item ** 2
# res = map(sq,l)
# print(list(res))
