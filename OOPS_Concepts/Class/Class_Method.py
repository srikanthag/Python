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

# Creating a class
class Student:
    school = 'Balwin'       # class variable

    def __int__(self, name, age):       # constructor
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, name):
        print(Student.school)   # access variable
        Student.school = name      # modifying the class variable

sri = Student()
Student.change_school("vidyavikas")

