# # #basics
# #
# class employee:
#     def __init__(self, fname, lname, pay):
#         self.first_name = fname       #instance variable
#         self.last_name = lname
#         self.salary = pay
#
#     def pay_hike(self, percentage):
#         hike = self.salary * percentage
#         self.salary = self.salary+hike
#         return self.salary
#
#     def email(self):
#         return f"{self.first_name}.{self.last_name}@gmail.com"
#
# emp1 = employee("srikanth", "jobs", 1000)     #inside storing as dictionary   #class
# emp2 = employee("srikanth1", "jobs1", 2000)
# # print(emp1.__dict__)
# #print(emp2.__dict__)
#
# #hike
# print(emp1.pay_hike(0.1))
# print(emp1.__dict__)
#
# print(emp2.pay_hike(0.2))
# print(emp2.__dict__)
#
# #email
# #emp1
# # print(employee.email(emp1))
# # #or
# # print(emp1.email())
# #
# # #emp2
# # print(employee.email(emp2))
# # #or
# # print(emp2.email())


# class calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
#     def sub(self):
#         return self.a - self.b
#
#     def div(self):
#         return self.a / self.b
#
#     def mul(self):
#         return self.a * self.b
#
# c1 = calculator(10,20)
# c2 = calculator(30,60)
# c3 = calculator(100,200)
# # print(dir(c1))
# # print(c1.__dict__)
# # print(c2.__dict__)
# # print(c3.__dict__)
#
# # print(c1.add())
# # print(c2.add())
# # print(c3.mul())
# # print(c3.div())

# class player:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = yield
#         self.health = 100
#
#     def move(self, dx, dy):
#         self.x += dx
#         self.y += dy
#
#     def attack(self, pts):
#         self.health -= pts
#
# p1 = player(1,2)
# p2 = player(3,4)
# p2 = player(5,6)


# class demo:
#     count = 0
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         demo.count = demo.count + 1


# class dog:
#     attr1 = 'bird'
#     def __init__(self, name):
#         self.name = name
#
# Rodger = dog("Rodger")
# Tommy = dog("Tommy")
# print(Rodger.__class__.attr1)
# print("Tommy is a {}".format(Tommy.__class__.attr1))
# print("My name is {}".format(Rodger.name))


#callable
# class squre:
#     def __call__(self, num):
#         self.num = num
#         for numer in num:
#             return num ** 2
# s = squre([1,2,3])
# print(s)





# class emp():
#     def __init__(self, name, sal):
#         self.name = name
#         self.sal = sal
#
#     def emil(self):
#         return f"{self.name}@gmail.com"
#
#
# mail = emp('srikanth', 100)
# e = (mail.emil())
# print(e)





