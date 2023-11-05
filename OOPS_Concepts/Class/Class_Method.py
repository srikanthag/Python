# Using classmethod() method
class Python:
    course = 'Algorithm'

    def algo(object_):
        print("This is an algorithm: ", object_.course)

# Creating a classmethod function by passing a method to it
Python.algo = classmethod(Python.algo)
Python.algo()

# ==========================================================================================

# Using @classmethod() method
from datetime import date

# Creating a class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Using the class method decorator to make the years of alumni class a class method class
    # Creating a class method.
    @classmethod
    def alumniYear(cls, name, year):
        return cls(name, date.today().year - year)

# Creating an instance of the class
person1 = Student.alumniYear('Louis', 1999)

print(person1.age)










