import re
# print(dir(re))

from re import findall

# e=re.findall(r"[aeiou]", "hi how are you")
# print(e)
#
# e = re.findall(r"aeiou", "hi how are you")
# print(e)

# e=re.findall(r"[how]", "hi how are you")
# print(e)

# e=re.findall(r"how", "hi how are you")
# print(e)

#find number
# e = re.findall(r"[0-9]", "hi how 99 are 100 you")
# print(e)

#find number 0 to 5
# e = re.findall(r"[0-5]", "hi how 99 are 100 you")
# print(e)

#find entire number (+)
# e = re.findall(r"[0-9]+", "hi how are 100 you")
# print(e)

#find only lower char in string
# e = re.findall(r"[a-z]", "hi HOW 99 are 100 you")
# print(e)

#find only upper char in string
# e = re.findall(r"[A-Z]", "hi HOW 99 are 100 you")
# print(e)

#find only upper and lower char in string
# e = re.findall(r"[A-Za-z]", "hi HOW 99 are 100 you")
# print(e)

#afind all except number
# e = re.findall(r"[^0-9]", "hi HOW@#$ 99 are 100 you")
# print(e)

# e = re.findall(r"[^0-9]+", "hi HOW@#$ 99 are 100 you")
# print(e)

#alphanumeric
# e = re.findall(r"[A-Za-z0-9]", "hi HOW@#$ 99 are 100 you")
# print(e)


#wordboundary
#get picode (six continous digit)
# sentance = "the pincode of bangalore is 560001 aaaaaa and the telephone code is 080 phone 9686612322"
# e = re.findall(r"\b\d{6}\b", sentance)
# print(e)


# sentance = "iam treaveling fro BLR to DHL on 26-JULy-2022"
# e = re.findall(r"\b[A-Z]{3}\b", sentance)
# print(e)

#2 and 5 char word
# e = re.findall(r"\b\w{2,5}\b", "hi hello and python is a programming language")
# print(e)

#grab 3 letter words
# e = re.findall(r"\b\w{3}\b", "hi hello and python is a programming language")
# print(e)


#grab minimum 3 character letter words
# e = re.findall(r"\b\w{3,}\b", "hi hello and python his a programming language")
# print(e)

#FIND all the words starts with 'h'
# sentance = "hi hello and python is a programming language"
# e = re.findall(r"\bh\w+", sentance)
# print(e)
#
#FIND all the words starts with vowels
# sentance = "hi hello and apython is a programming language"
# e = re.findall(r"\b[aeiou]\w+", sentance)
# print(e)

#FIND all the words starts with consonents
# sentance = "hi hello and apython is a programming language"
# e = re.findall(r"\b[^aeiou\s]\w+", sentance)
# print(e)


#find all words ends with 'o'
# sentance = "hi hello and apython is a oprogramming language ohio"
# e = re.findall(r"\b\w+o\b", sentance)
# print(e)


#count individual number number
# word = "sony india pvt34 Ltd567 Bangalore"
# e = re.findall(r"\d", word)
# print(e)
# total = 0
# for item in e:
#     total += int(item)
# print(total)

#count number set
# word = "sony123 india pvt34 Ltd567 Bangalore"
# e = re.findall(r"\d+", word)
# print(e)
# total = 0
# for item in e:
#     total += int(item)
# print(total)


#count number space
# word = "sony123 india pvt34 Ltd567 Bangalore"
# e = re.findall(r"\s", word)
# print(len(e))

#wap count non special char
# word = "sony123 india pvt34#$% Ltd567 Bangalore"
# e = re.findall(r"\w", word)
# d = {item:e.count(item) for item in e}
# print(d)

#all char except digits
# word = "sony123 india pvt34#$% Ltd567 Bangalore"
# e = re.findall(r"\d", word)
# d = {item:e.count(item) for item in e}
# print(d)

#filter char returns in string
# word = "sony123 india pvt34#$% Ltd567 Bangalore"
# e = re.findall(r"\D", word)
# s = ''.join(e)
# print(s)
# print(type(s))

#count the char in each word. ignore special character
# word = "sony india pvt#$% Ltd Bangalore"
# e = re.findall(r"\b\w+\b", word)
# d = {item:len(item) for item in e}
# print(d)


#count the total number of upper and lower char
# word = "sony india pvt#$% Ltd Bangalore"
# e = re.findall(r"[A-Z]", word)
# a = re.findall(r"[a-z]", word)
# print(len(e))
# print(len(a))

#downloading_messages
# word = """hi hiw hurnr.zip
# hyebrtd fgeteh bfge.httr
# fjdhrtnm nfhtefwsvb.com
# kju hgg jjggy.jy"""
#
# e = re.findall(r"\.[a-zA-Z]+", word)
# print(e)









