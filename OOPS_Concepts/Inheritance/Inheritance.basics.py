# class parent:
#     def __init__(self, value):
#         self.value = value
#
#     def google(self):
#         print(f"executing parent google {self.value}")
#
#     def apple(self):
#         print(f"executing parent apple")
#         self.google()
#
# p = parent(10)
# print(p.google())
# print(p.apple())
#
# # #child1 Class having separate method called demo
#
# class child1(parent):
#     def demo(self):
#         print("execute demo")
# c1 = child1(10)
# print(c1.google())
# print(c1.apple())
# print(c1.demo())
# print(c1.__init__)
# #
#
# #overriding parent Class method
#
# class child2(parent):
#     def demo(self):
#         print("execute demo")
#
#     def google(self):
#         print(f"executing child2 google {self.value}")
#
# c2 = child2(10)
# print(c2.google())
# print(c2.apple())
# #
# # #child adding extra functionality and reused original functionality of parent
# class child3(parent):
#     def google(self):
#         print("executing child 3 google")
#         super().google()                #   super is used to acces parent Class attributes
#
# c3 = child3(10)
# print(child3.__mro__)                      #mro -method resalution order
# print(c3.google())
# print(c3.apple())
# #
# # #child Class having extra attributes
# class child4(parent):
#     def __init__(self, value, name):
#         self.name = name
#         super().__init__(value)              #calling parent Class constructor
#
# c4 = child4(10, 'srikanth')
# print(c4.name)
# print(c4.value)
#
#
# Class facebook:
#     def spam(self):
#         print("executing facebook spam")
#
#
# #child inheriting from multiple Inheritance
# Class child5(parent, facebook):
#     pass
#
# c5 = child5(10)
# print(c5.spam())
# print(c5.google())
# print(c5.apple())




#multi-level Inheritance
class a:
    def demo(self):
        print("Class a demo")

class b(a):
    def demo(self):
        print("Class b demo")
        super().demo()

class c(b):
    def demo(self):
        print("Class c demo")
        super().demo()

c1= a()
print(c1.demo())
c2 = b()
print(c2.demo())
c3 = c()
print(c3.demo())

# Class parent:
#     def demo(self):
#         print("Class parent demo")
#
# Class child1(parent):
#     def demo(self):
#         print("Class child1 demo")
#         super().demo()
#
#
# Class child2(parent):
#     def demo(self):
#         print("Class child2 demo")
#         super().demo()
#
# #multiple Inheritance
# Class parent2(child1, child2):
#     pass



