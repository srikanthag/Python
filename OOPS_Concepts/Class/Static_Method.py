# Using staticmethod() method

class Marks:
    def Math_num(a, b): # define the static Math_num() function
        return a + b

    def Sci_num(a, b): # define the static Sci_num() function
        return a + b

    def Eng_num(a, b):  # define the static Eng_num() function
        return a + b

# create Math_num as static method
Marks.Math_num = staticmethod(Marks.Math_num)

# print the total marks in Maths
print (" Total Marks in Maths" , Marks.Math_num(64, 28))

# create Sci_num as static method
Marks.Sci_num = staticmethod(Marks.Sci_num)

# print the total marks in Science
print (" Total Marks in Science" , Marks.Sci_num(70, 25))

# create Eng_num as static method
Marks.Eng_num = staticmethod(Marks.Eng_num)

# print the total marks in English
print (" Total Marks in English" , Marks.Eng_num(65, 30))


# ============================================================================
# Using  @staticmethod

class Marks:
    @staticmethod
    def Math_num(a, b): # define the static Math_num() function
        return a + b

    @staticmethod
    def Sci_num(a, b): # define the static Sci_num() function
        return a + b

    @staticmethod
    def Eng_num(a, b):  # define the static Eng_num() function
        return a + b

# print the total marks in Maths
print (Marks.Math_num(64, 28))

# print the total marks in Science
print (Marks.Sci_num(70, 25))

# print the total marks in English
print (Marks.Eng_num(65, 30))

