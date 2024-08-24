path = r"C:\Users\srikanth\Desktop\IT\Python\python_practice\python_class\file_directory\txt_log_files\sample.txt"
path2 = r"C:\Users\srikanth\Desktop\IT\Python\python_practice\python_class\file_directory\txt_log_files\access-log.txt"
path3 = r"C:\Users\srikanth\Desktop\IT\Python\python_practice\python_class\file_directory\txt_log_files\sample.log"
path4 = r"C:\Users\srikanth\Desktop\IT\Python\python_practice\python_class\file_directory\txt_log_files\football.txt"

# 1. wap to read all the lines in a file without loading the file into memory
with open(path) as file:
    for line in file:
        print(line)

# 2. wap to count the number of lines present in the file
with open(path) as file:
    count = 0
    for line in file:
        count += 1
    print(count)

# 3. wap to print line number and line from the file
with open(path) as file:
    count = 0
    for line in file:
        count += 1
        print(count, line)

# Alternate

with open(path) as file:
    for line_no, line in enumerate(file, start=1):
        print(line_no, line)


# 4. wap to count the number of words in the given file
with open(path) as file:
    count = 0
    for line in file:
        d = line.split()
        for word in d:
            count += 1
    print(count)

# Alternate
with open(path) as file:
    count = 0
    for line in file:
        d = line.split()
        count += len(d)
    print(count)

# 5. wap to print the lines from the last of file
with open(path) as file:
    res = reversed(list(file))
    for line in file:
        print(line)

# 6. wap to count the number of spaces in the given file
with open(path) as file:
    count = 0
    for line in file:
        for char in line:
            if char == " ":
                count += 1
    print(count)

# Alternate
with open(path) as file:
    count = 0
    for line in file:
        spaces = line.count(" ")
        count += spaces
    print(count)

# 7. wap to count the number of words that are starting with vowels
with open(path) as file:
    count = 0
    for line in file:
        for word in line.split():
            if word[0] in 'aeiouAEIOU':
                count += 1
    print(count)

# 8. wap to create a dictionary of word and its count pair in the given file

with open(path) as file:
    d = {}
    for line in file:
        words = line.split()
        for word in words:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
    print(d)

# Alternate
from collections import defaultdict, Counter

with open(path) as file:
    dd = defaultdict(int)
    for line in file:
        for word in line.split():
            dd[word] += 1
    print(dd)

# 9. wap to extract all the ip address from asscess.log.txt file (list of ip address)
with open(path2) as file:
    l = []
    for line in file:
        if line.strip():            #to find out empty line [important]
            s = line.split()
            l.append(s[0])
    # print(l)

# 10. wap to create a dictionary of ip adress and their count pair
with open(path2) as file:
    d = {}
    for line in file:
        if line.strip():
            words = line.split()
            if words[0] not in d:
                d[words[0]] = 1
            else:
                d[words[0]] += 1
    print(d)

#counter Class
from collections import Counter
with open(path2) as file:
    l = []
    for line in file:
        if line.strip():
            s = line.split()
            l.append(s[0])
    # print(l)
ip_ = Counter(l)
print(ip_)

# list of tuple
from collections import Counter
with open(path2) as file:
    l = []
    for line in file:
        if line.strip():
            s = line.split()
            l.append(s[0])
    # print(l)
ip_ = Counter(l)
print(ip_.most_common(5))

# 11. wap to print n th line in a file
with open(path) as file:
    n = 3
    for line_no, line in enumerate(file, start=1):
        if line_no == n:
            print(line)

# using count
with open(path) as file:
    n = 3
    count = 0
    for line in file:
        count += 1
        if count == n:
            print(line)
            break

#using islice
from itertools import islice
n = 3
with open(path) as file:
    res = islice(file, n, n+1)
    print(list(res))

# 12. wap to print first n lines
#using isslice
from itertools import islice
n = 3
with open(path) as file:
    res = islice(file, n)
    print(list(res))

#or using enumerate
n= 3
with open(path) as file:
    for lineno, line in enumerate(file, start=1):
        if lineno <= n:
            print(line)

# 13. wap to print last n lines
from itertools import islice
n= 3
with open(path) as file:
    count = 0
    for line in file:
        count += 1
    file.seek(0)
    res = islice(file, count-1, count)
    print(list(res))

#using deque
from collections import deque
n = 5
with open(path) as file:
    lines = deque(file, n)
    print(list(lines))

# 14. finding the length of each line in the TEXT file
with open(path) as file:
    for line in file:
        print(line, len(line))

# 15. extracting message from sample.log
with open(path3) as file:
    for line in file:
        s = line.split()
        print(s[2])

# 16. counting number of INFO, WARN, TRACE messages
with open(path3) as file:
    count = 0
    for line in file:
        s = line.split()
        count += 1
    print(count)

from collections import Counter
with open(path3) as file:
    l = []
    for line in file:
        if line.strip():
            s = line.split()
            l.append(s[2])
res = Counter(l)
print(res)

# 17. reading countries from football.txt
with open(path4, encoding="UTF-8") as file:
    for line in file:
        if line.strip():
            s = line.split("\t")
            print(s[1])

# 18. least and most occurrence of the word
from collections import Counter
from collections import defaultdict
with open(path) as file:
    d = defaultdict(int)
    for line in file:
        if line.strip():
            s = line.split()
            for item in s:
                d[item] += 1
print(d)
res = Counter(d)
most, *rest, least = res.most_common()

print(most, least)

# 19. tell and seek
with open(path) as file:
    data = file.readlines()
    print(data)
    print(file.tell())
    file.seek(20)
    print(file.seek(20))
