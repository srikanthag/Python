# 1. wa set Comprehension to create a set of squres from i to 10
s = {i ** 2 for i in range(0, 11)}
print(s)


# 2. wa set Comprehension to create set of tuples item of index and the item
s = {1,2,3,4}
se = {(item, s[item]) for item in range(len(s))}
print(se)

# enumerate
se = {item for item in enumerate(s)}
print(se)

# wa set Comprehension to create set of tuples with item and its length pair
s = {'amazon', 'srikanth', 'mysore'}
se = {(item, len(item)) for item in s}
print(se)
