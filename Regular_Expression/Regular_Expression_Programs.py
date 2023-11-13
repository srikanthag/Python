import re
# print(dir(re))

# 1. find number 0 to 5
# e = re.findall(r"[0-5]", "hi how 99 are 100 you")
# print(e)

# 2. find entire number (+)
# e = re.findall(r"[0-9]+", "hi how are 100 you")
# print(e)

# 3. find only lower char in string
# e = re.findall(r"[a-z]", "hi HOW 99 are 100 you")
# print(e)

# 4. find only upper char in string
# e = re.findall(r"[A-Z]", "hi HOW 99 are 100 you")
# print(e)

# 5. find only upper and lower char in string
# e = re.findall(r"[A-Za-z]", "hi HOW 99 are 100 you")
# print(e)

# 6. find all except number
# e = re.findall(r"[^0-9]", "hi HOW@#$ 99 are 100 you")
# print(e)

# 7. find alphanumeric
# e = re.findall(r"[A-Za-z0-9]", "hi HOW@#$ 99 are 100 you")
# print(e)

''' wordboundary '''
# 8. get pincode (six continuous digit)
# sentance = "the pincode of bangalore is 560001 aaaaaa and the telephone code is 080 phone 9686612322"
# e = re.findall(r"\b\d{6}\b", sentance)
# print(e)

# 9. 2 and 5 char word
# e = re.findall(r"\b\w{2,5}\b", "hi hello and python is a programming language")
# print(e)

# 10. grab 3-letters words
# e = re.findall(r"\b\w{3}\b", "hi hello and python is a programming language")
# print(e)


# 11. grab minimum 3-character letter words
# e = re.findall(r"\b\w{3,}\b", "hi hello and python his a programming language")
# print(e)

# 12. find all the words starts with 'h'
# sentence = "hi hello and python is a programming language"
# e = re.findall(r"\bh\w+", sentence)
# print(e)

# 13. find all the words starts with vowels
# sentence = "hi hello and a python is a programming language"
# e = re.findall(r"\b[aeiou]\w+", sentence)
# print(e)

# 14. find all the words starts with consonants
# sentence = "hi hello and a python is a programming language"
# e = re.findall(r"\b[^aeiou\s]\w+", sentence)
# print(e)


# 15. find all words ends with 'o'
# sentance = "hi hello and apython is a oprogramming language ohio"
# e = re.findall(r"\b\w+o\b", sentance)
# print(e)


# 16. count individual number
# word = "sony india pvt34 Ltd567 Bangalore"
# e = re.findall(r"\d", word)
# print(e)
# total = 0
# for item in e:
#     total += int(item)
# print(total)

# 17. count number set
# word = "sony123 india pvt34 Ltd567 Bangalore"
# e = re.findall(r"\d+", word)
# print(e)
# total = 0
# for item in e:
#     total += int(item)
# print(total)


# 18. count number space
# word = "sony123 india pvt34 Ltd567 Bangalore"
# e = re.findall(r"\s", word)
# print(len(e))

# 19. wap count non-special char
# word = "sony123 india pvt34#$% Ltd567 Bangalore"
# e = re.findall(r"\w", word)
# d = {item:e.count(item) for item in e}
# print(d)

# 20. fill all char except digits
# word = "sony123 india pvt34#$% Ltd567 Bangalore"
# e = re.findall(r"\D", word)
# d = {item:e.count(item) for item in e}
# print(d)

# 21. filter char returns in string
# word = "sony123 india pvt34#$% Ltd567 Bangalore"
# e = re.findall(r"\D", word)
# s = ''.join(e)
# print(s)
# print(type(s))

# 22. count the char in each word. ignore special character
# word = "sony india pvt#$% Ltd Bangalore"
# e = re.findall(r"\b\w+\b", word)
# d = {item:len(item) for item in e}
# print(d)


# 23. count the total number of upper and lower char
# word = "sony india pvt#$% Ltd Bangalore"
# e = re.findall(r"[A-Z]", word)
# a = re.findall(r"[a-z]", word)
# print(len(e))
# print(len(a))

# 24. downloading_messages
# word = """hi hiw hurnr.zip
# hyebrtd fgeteh bfge.httr
# fjdhrtnm nfhtefwsvb.com
# kju hgg jjggy.jy"""
#
# e = re.findall(r"\.[a-zA-Z]+", word)
# print(e)


# 25.  Matches any character except new line
# r = re.findall(r'.', "hello world")
# print(r)

# 26. find one char after h
# r = re.findall(r'h.', "hello")
# print(r)


# 27. find any one char between 2 char
# r = re.findall(r'a.b', "acb gg abbr")
# print(r)

# 28. find any n number of char between 2 char
# r = re.findall(r'a.*a', "annnnnna")
# print(r)

# 29. find first char
# r = re.findall(r"^hello", "hello world hello")
# print(r)

# 30. find last char
# r = re.findall(r"world$", "hello world")
# print(r)







