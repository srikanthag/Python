"""Global variable"""
# In Python, a global variable is a variable that is defined outside any function or block of code. It is accessible from any part of the code, including inside functions, as long as the function doesn't define a local variable with the same name.
# Global variables can be used inside or outside the function.


a = 10
# accessing is a global variable inside function
def spam():
    print(a)
spam()
print(a)

# Global variables can be accessed and modified by any function in the script, making them shared across the entire program.
# Use the global keyword inside functions to modify a global variable.

# modify global variable
def spam():
    global a
    a = a + 5
    print(a)
spam()
print(a)
