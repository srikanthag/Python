#  1. AssertionError: Raised when the assert statement fails.
# x = 1
# y = 0
# assert y != 0, "Invalid Operation" # denominator can't be 0

#  2. AttributeError: Raised on the attribute assignment or reference fails.
# X = 10
# Raises an AttributeError
# X.append(6)
# Error_Message: AttributeError: 'int' object has no attribute 'append'

#  3. ImportError (ModuleNotFoundError): Raised when the imported module is not found.
# import Mathematics
# from math import *
# print(pi)
# print(factorial(6))
# Error_Message: ModuleNotFoundError: No module named 'mathematics'

#  4. IndexError: Raised when the index of a sequence is out of range.
# fruits = ['Apple', 'Banana', 'Guava']
# print(fruits[8])
# Error_Message: IndexError: list index out of range

#  5. KeyError: Raised when a key is not found in a dictionary.
# dict = {'a':1, 'b':2}
# print(dict['c'])
# Error_Message: KeyError: 'c'

#  5. NameError: Raised when a variable is not found in the local or global scope.
# print(geek)
# geek = "GeeksforGeeks"
# Error_Message: NameError: name 'geek' is not defined


#  6. SyntaxError: Raised by the parser when a syntax error is encountered.
# a = 'sri'
# print(s
# Error_Message: SyntaxError: '(' was never closed

#  7. IndentationError: Raised when there is an incorrect indentation.
# a = 'sri'
# for item in a:
# print(a)
# Error_Message: IndentationError: expected an indented block after 'for' statement on line 2

#  8. SystemError: Raised when the interpreter detects internal error.

#  9. TypeError: Raised when a function or operation is applied to an object of an incorrect type.
# geek = "Geeks"
# num = 4
# print(geek + num + geek)
# Error_Message: can only concatenate str (not "int") to str

#  10. UnicodeError: Raised when a Unicode-related encoding or decoding error occurs.
# t = b"a".decode("ascii")
# t1 = b"a\xf1".decode("ascii")
# Error_Message: UnicodeDecodeError: 'ascii' codec can't decode byte 0xf1 in position 1: ordinal not in range(128)

#  11. ValueError: Raised when a function gets an argument of correct type but improper value.
# import math
# print(math.sqrt(-9))
# Error_Message: ValueError: math domain error

#  12. ZeroDivisionError: Raised when the second operand of a division or module operation is zero
# a = 4
# b = 0
# print(a/b)
# Error_Message: ZeroDivisionError: division by zero

