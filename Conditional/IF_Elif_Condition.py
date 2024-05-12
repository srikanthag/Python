# 1. wap to check if the given input number is even or odd
number = 3
if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")

# 2. to check if the character is lowercase or uppercase
char = "r"
if "a" <= char <= "z":
    print(f"{char} is lowercase")
else:
    if "A" <= char <= "Z":
        print(f"{char} is uppercase")
    else:
        print(f"{char} is not an alphabet")

# 3. to check if the given iterable is empty or not
iterable = "hai"
if len(iterable) > 0:
    print("the iterable is not empty")

else:
    print("iterable is empty")

# 4. to check if the given value is default or non default value
value = []
if value:
    print("It is non default value")
else:
    print("default value")


# 5. wap to convert lowercase to uppercase and vice-versa
char = "N"
if char.islower():
    upper_char = char.upper()
    print(upper_char)

elif char.isupper():
    lower_char = char.lower()
    print(lower_char)

else:
    print("character is not an alphabet")

char = "n"

if "a" <= char <= "z":
    print(chr(ord(char) - 32))

elif "A" <= char <= "Z":
    print(chr(ord(char) + 32))

else:
    print("character is not an alphabet")

# 6.wap to check if the iterable has even-number of elements
list_ = [10, 20, 30, 40]

if len(list_) % 2 == 0:
    print("iterable has even numbered elements")
else:
    print("iterable has odd numbered elements")

# 7. to check if the first digit in the given number is even or odd """
number = 1234
str_num = str(number)
if int(str_num[0]) % 2 == 0:
    print("number is even")
else:
    print("number is odd")

print("number is even" if int(str_num[0]) % 2 == 0 else "number is odd")
