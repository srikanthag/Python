sentence = 'hello 123 world 567 welcome to 9724 py'
import re
d = re.findall(r'\d', sentence)
# print(d)
dd = {}
for index, item in enumerate(d):
    dd[item] = index
print(dd)






















