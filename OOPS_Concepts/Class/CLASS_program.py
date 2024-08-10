
class employee:
    def __init__(self, fname, lname, pay):
        self.first_name = fname       #instance variable
        self.last_name = lname
        self.salary = pay

    def pay_hike(self, percentage):
        hike = self.salary * percentage
        self.salary = self.salary+hike
        return self.salary

    def email(self):
        return f"{self.first_name}.{self.last_name}@gmail.com"

emp1 = employee("srikanth", "jobs", 1000)     #inside storing as dictionary   #Class
emp2 = employee("srikanth1", "jobs1", 2000)
# print(emp1.__dict__)
#print(emp2.__dict__)

#hike
print(emp1.pay_hike(0.1))
print(emp1.__dict__)

print(emp2.pay_hike(0.2))
print(emp2.__dict__)

# email
# emp1
print(employee.email(emp1))
#or
print(emp1.email())

#emp2
print(employee.email(emp2))
#or
print(emp2.email())


# ============================================================================================================

class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def div(self):
        return self.a / self.b

    def mul(self):
        return self.a * self.b

c1 = calculator(10,20)
c2 = calculator(30,60)
c3 = calculator(100,200)
# print(dir(c1))
# print(c1.__dict__)
# print(c2.__dict__)
# print(c3.__dict__)

print(c1.add())
print(c2.add())
print(c3.mul())
print(c3.div())

# =============================================================================================================

class player:
    def __init__(self, x, y):
        self.x = x
        self.y = yield
        self.health = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def attack(self, pts):
        self.health -= pts

p1 = player(1,2)
p2 = player(3,4)
p3 = player(5,6)

# =============================================================================================================

class emp():
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal

    def emil(self):
        return f"{self.name}@gmail.com"


mail = emp('srikanth', 100)
e = (mail.emil())
print(e)

# =============================================================================================================

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Deposit amount should be greater than 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount for withdrawal.")

    def check_balance(self):
        print(f"Account Balance for {self.account_holder}: ${self.balance}")

account1 = BankAccount("123456", "Alice", 1000)

# Depositing and withdrawing
account1.deposit(500)
account1.withdraw(200)
account1.check_balance()
