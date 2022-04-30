class bank_account:
    intrerest_rate = 0.04
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError('amount should be greater than zero')
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            raise ValueError('insuficient funds')

    def roi(self):
        intrest_amount = self.balance * self.__class__.intrerest_rate
        self.balance += intrest_amount

# b = bank_account('srikanth', 20000)


# class SBAaccount(bank_account):
#     intrerest_rate = 0.05   #redefining class variable
#     def withdraw(self, amount):
#         if amount > 1000:
#             raise ValueError("caanot withdraw more than 10k")
#         super().withdraw(amount)

# sa = SBAaccount('srikanth', 20000)
# print(sa.withdraw(200))
# print(sa.roi())
# print(sa.balance)


# class salary_acount(bank_account):
#     def withdraw(self, name):
#         self.is_first_month_sal = True
#         self. max_draft_amount = 0.0
#         super().__init__(name, 0.00)
#
#     def deposit(self, amount):
#         if self.is_first_month_sal:
#             self.is_first_month_sal = False
#             super().__init__(amount + 1000)
#         else:
#             super().deposit(amount)
#
#     def overdraft(self, amount):
#         if amount <= self.max_draft_amount:
#             super().withdraw(amount)
#             self.max_draft_amount -= amount
#         else:
#             raise ValueError(f"max available draft amount in {self.max_draft_amount}")

# sal = bank_account('srikanth', 0.00)
# print(sal.balance)
# print(sal.deposit(2500))
# print(sal.__dict__)
# print(sal.withdraw(300))
# print(sal.balance)
# print(sal.overdraft())


# class senior_citizen(bank_account):
#     intrerest_rate = 0.06
#     def withdraw(self, amount):
#         if amount > 2000:
#             raise ValueError("caanot withdraw more than 20k")
#         super(). withdraw(amount)
#
# sc = senior_citizen('srikanth', 20000)
# print(sc.withdraw(2000))
# print(sc.roi())
# print(sc.balance)


class sukanyasamruddi(bank_account):

    def deposit(self, amount):
        if amount < 1000:
            raise ValueError("min amount is deposit is 1k")
        super().deposit(amount)
    #
    def withdraw(self, amount):
            raise TransactionDeclined("you cannot withdraw from SSA")



sk = bank_account('unnati', 0.0)
print(sk.deposit(350))

print(sk.withdraw(55))
# print(sk.balance)








