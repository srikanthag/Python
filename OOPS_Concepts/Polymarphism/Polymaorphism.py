class Polymarph:
     def __init__(self, a, b):
         self.a = a
         self.b = b

     def add(self):
         return self.a + self.b

pol = Polymarph([1,2],[3,4])
print(pol.add())

pol = Polymarph(3,4)
print(pol.add())
