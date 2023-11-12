class CubeDecorator:  
    def __init__(self, function):  
        self.function = function  
  
    def __call__(self, *args, **kwargs):
        # before function  
        result = self.function(*args, **kwargs)
        # after function  
        return result

# adding class decorator to the function

@CubeDecorator  
def get_cube(n):  
    print("given number is:", n)  
    return n * n * n  
  
print("Cube of number is:", get_cube(25))  

# In the above code, we have created CubeDecorataor class as a decorator and called the __call__() method.
# In the __call__() we called the caller function and return the result.
