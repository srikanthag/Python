# 1. Protected members
class BankAccount:
    _intrest = 4.5           #internal implimentation only #you are not supose to attribute out side the Class but u will be
    # acess and also modify the attribute value also
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

     #internal purpose only
    def _spam(self):
        print("bank account executiong _spam")

    def demo(self):
        print(self._intrest)
        print(self._spam())


class SBaccount(BankAccount):
    _intrest = 6.5              #overiding _interest rate in child Class

    def _spam(self): #overriding _spam
        print("sbaccount _spam")


# b = BankAccount('srikanth', 1200)
# print(type(b))
# print(b.__dict__)
# # print(BankAccount.__dict__)
# print(b.demo())
# print(b._spam())
#
b1 = SBaccount('srikantn', 1000)
print(b1._spam())
print(b1.demo())


# ===============================================================================================================


# # 2. Private members
#
# class BankAccount:
#     __intrest = 4.5
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#      #internal purpose only
#
#     def __spam(self):
#         print("bank account executiong _spam")
#
#     def demo(self):
#         print(self.__intrest)
#         self.__spam()
#
# class SBaccount(BankAccount):
#     __intrest = 6.5 #overiding _interest rate in child Class
#
#     def __spam(self): #overriding _spam
#         print("sbaccount __spam")
#
# b = BankAccount('srikanth', 1200)
# print(type(b))
# print(b.__dict__)
# print(BankAccount.__dict__)
# print(b.demo())
# print(b.__spam())
#
# b1 = SBaccount('srikantn', 1000)
# print(b1.__spam())
# print(b1.demo())



