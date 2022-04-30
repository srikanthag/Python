class shoping_cart:
    products = {"iphone": 10, "nokia": 9}
    price = {"iphone": 800, "nokia": 200}
    
    def __init__(self):
        self.cart = []

    def add_item(self, name, quantity):
        if name not in self.__class__.products:
            raise Exception("ivalid product")
        elif quantity <= self.__class__.products[name]:
            self.cart.append({"name": name, "quantity": quantity, "price": self.__class__.price[name]})
            self.__class__.products[name] -= quantity
        else:
            raise ValueError("product out of stock")

    def total_cost(self):
        total = 0.00
        for item in self.cart:
            total = total + (item["quantity"] * item["price"])
        return total

    def remove_item(self, name):
        for item in self.cart:
            if item["name"] == name:
                if item["quantity"] > 1:
                    item["quantity"] -= 1
                else:
                    self.cart.remove(item)


c1 = shoping_cart()
c2 = shoping_cart()
c3 = shoping_cart()

print(c1.__dict__)
print(c2.__dict__)
print(c3.__dict__)

#add
print(c1.add_item("iphone", 2))


print(c1.add_item("nokia", 3))

print(c1.__dict__)

#total
print(c1.total_cost())

#remove
print(c1.remove_item('nokia'))
print(c1.cart)

print(shoping_cart.products)







