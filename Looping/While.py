# 1. wap to print 10 to 1
n = 10
while n > 0:
    print(n)
    n-=1

# 2. wap to print -1 to -10
n = -1
while n >= -10:
    print(n)
    n-=1
for item in range(-10, 0):
    print(item)

# 3. wap to print 1 to 10
n = 1
while n <= 10:
    print(n)
    n+=1

# 4. wap to print -10 to -1
n = -10
while n <= -1:
    print(n)
    n+=1

# 5. wap to print even numbers from 1 to 50
n = 1
while n <=50:
    if n % 2 ==0:
        print(n)
    n+=1

# 6. wap to print odd numbers
n = 1
while n <= 50:
    if n % 2 != 0:
        print(n)
    n += 1

# 7. wap to print all the character in the string
a = "srikanth"
i = 0
while i < len(a):
    print(a[i])
    i += 1

# 8. wap to print all the character in the list
l = [1, 2, 3, 'sri']
i = 0
while i < len(l):
    print(l[i])
    i += 1

# 9. wap to print all the character in the list
t = (1, 2, 3, 4)
i = 0
while i < len(t):
    print(t[i])
    i += 1
