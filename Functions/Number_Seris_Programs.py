"Fibonacci series: The Fibonacci Sequence is a set of steadily increasing numbers where each number is equal to the sum of the preceding two numbers"

# 1. waf to print febnocii number series
def febonocii(num):
     a = 0
     b = 1
     i = 0
     while i <= num:
         print(a)
         c = a + b
         a = b
         b = c
         i += 1
febonocii(10)

# 2. waf that checks if the given number is fibonocii number or not
def febonocii(num):
     a = 0
     b = 1
     while a <= num:
         c = a + b
         a = b
         b = c
         if a == num:
             print(num, 'is a febenocii number')
             break
     else:
            print(num, 'not febenocii number')
febonocii(10)

# 3. waf that checks if the given number is fibonocii number or not
def febonocii(num):
    a = 0
    b = 1
    while a <= num:
        c = a + b
        a = b
        b = c
        if a == num:
            print(num, 'is a febenocii number')
            break
    else:
        print(num, 'not febenocii number')
febonocii(10)

# 4. waf to print fibonacci seris in the user defined range
def fib(end, start=0):
    a = 0
    b = 1
    i = 0
    while i < end:
        c = a + b
        a = b
        b = c
        i += c
    return a
print(fib(10))


"Prime number: Prime numbers are natural numbers that are divisible by only 1 and the number itself."

# 5. wa function that returns all the prime numbers in user defined range if the user doesn't start index take it a 2 and create a list
def prime(end, start = 2):
    l = []
    for n in range(start, end + 1):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                l.append(n)
    return l
print(prime(start=1, end=30))

#  6. wap to print whether prime or not
n = 10
for item in range(2, n):
    if n % item == 0:
        print('not a prime number')
        break
else:
    print('prime number')

# 7. wap to generate series of prime number
for n in range(15):
    if n > 1:
        for item in range(2, n):
            if n % item == 0:
                break
        else:
            print(n)

# 8. wap to print the prime number in the given sequence
l = [1, 2, 3, 4, 5, 6, 98, 45]
for item in l:
    if item > 1:
        for i in range(2, item):
            if item % i == 0:
                print(item, 'not a prime number')
                break
        else:
            print(item, 'prime number')


"Factorial numbe: The factorial of a whole number is the function that multiplies the number by every natural number below it."

# 9. ''' waf to print factorial number '''
def fact(n):
     if n == 0:
         return 1
     return n * fact(n-1)
print(fact(5))
