import re
# . - Matches any character except new line
# r = re.findall(r'.', "hello world")
# print(r)

#one char after h
# r = re.findall(r'h.', "hello")
# print(r)

# r = re.findall(r'h.', "hello world hi how how are you")
# print(r)

#find any one char between 2 char
# r = re.findall(r'a.b', "acb gg abbr")
# print(r)

#find any n number of char between 2 char
# r = re.findall(r'a.*a', "annnnnna")
# print(r)

#find first char
# r = re.findall(r"^hello", "hello world hello")
# print(r)

#find last char
# r = re.findall(r"world$", "hello world")
# print(r)


