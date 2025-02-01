"""Local variable"""
# In Python, a local variable is a variable that is defined within a function or a block of code and is only accessible within that function or block. It’s created when the function is called and destroyed when the function finishes execution.
# Defining local variables. They have scope only within a function

def add():
    a = 20
    b = 30
    c = a + b
    print("The sum is:", c)

add()       # When the function add() is called, Python executes the code inside the function. It first assigns 20 to a, 30            to b, and then calculates c as the sum of a and b (i.e., 20 + 30 = 50).
# print(a)    # This will raise an error because 'a' is not defined outside the function
# print(b)    # This will raise an error because 'a' is not defined outside the function