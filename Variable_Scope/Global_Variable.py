"Global variable"
# Global variables can be utilized all through the program, and its extension is in the whole program.
# Global variables can be used inside or outside the function.


a = 10
# accessing is a global variable inside function
def spam():
    print(a)
spam()

# modify global variable
def spam():
    global a
    a = a + 5
    print(a)
spam()
