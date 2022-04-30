#wa set comprehension to create a set of squres from i to 10
#normal
# r = set()
# for i in range(0, 11):
#     r.add(i**2)
# print(r)

#compreshension
# s = {i ** 2 for i in range(0, 11)}
# print(s)


#wa set comprension to create set of tuples item of index and the item
# s = {1,2,3,4}
# se = {(item, s[item]) for item in range(len(s))}
# print(se)

# se = {item for item in enumerate(s)}
# print(se)

#wa set comprenhision to create set of tuples with item and its length pair
# s = {'amezon', 'srikanth', 'mysore'}
# se = {(item, len(item)) for item in s}
# print(se)