

    def withdraw(self, amount):
        if amount > self.baclass Bankaccount:
    intrest_rate = 0.04      #class variable

    def __init__(self, name, balance=0):
        #instance variable
        self.name = name
        self.balance = balance
        self.tranasaction = []
        self.tranasaction.append(f"{name} initial amount depesited {balance}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.tranasaction.append(f"ammounted deposited {amount}")lance:
            raise ValueError("insufficient funds")
        self.balance = self.balance - amount
        self.tranasaction.append(f"amount withdraw {amount}")
        return f"please collect the ammount {amount}"

    def tranfer(self, to_account, amount):
        if self.balance < amount:
            raise ValueError("insuficient funds")
        to_account.deposit(amount)
        self.balance -= amount

    def statement(self):
        for tranasaction in self.tranasaction:
            print(tranasaction)
        print("*" * 20)
        print(f"available balance is {self.balance}")

    def roi(self):
        intrest_amount = self.balance * Bankaccount.intrest_rate
        self.balance += self.balance + intrest_amount
        self.tranasaction.append(f"**Intrest amount credited***{intrest_amount}")



c1 = Bankaccount('srikanth', 1000)
c2 = Bankaccount('rohitsharma', 2000)
c3 = Bankaccount('sharath')

# print(c1.__dict__)
# print(c2.__dict__)
# print(c3.__dict__)

#deposite
# print(c1.deposit(250))
# print(c1.__dict__)

# withdraw
# print(c1.withdraw(250))
# print(c1.__dict__)

# print(c1.withdraw(2250))
# print(c1.__dict__)

# for tranaction in c1.tranasaction:
#     print(tranaction)

# print(c1)
# print(c2)
# print(c3)

# print(c1.tranfer(c2, 100))
# print(c2.balance)
# print(c1.balance)

# print(c1.tranfer(c3, 500))
# print(c3.balance)
# print(c1.balance)

# print(c2.tranfer(c1, 800))
# print(c2.statement())
# print(c1.statement())


# print(c1.roi())
# print(c1.balance)







