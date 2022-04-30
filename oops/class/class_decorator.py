# class count:
#     def __init__(self, func):

# item = ['vu','uv', 'dt', 'cu']
# def get_last(chr):
#     return item[-1]
#
# class getlast:
#     def __call__(self, item):
#         return item[-1]
#
# lambda.get_last = lambda item:item[-1]
#
# g = getlast()
# by_last = sorted(item, key=g)
# by_last = sorted(item, key=get_last)
# by_last = sorted(item, key=lambda_get_last)




l = [{'name': 'Ram', 'class': 6, 'age': 12 },
    {'name': 'Sham', 'class': 12, 'age': 18 },
    {'name': 'John', 'class': 8, 'age': 13 } ]

print(sorted(l, key=lambda item: item['class']))
print(sorted(l, key=lambda item: item['age']))
print(sorted(l, key=lambda item: item['name']))

def get_name(item):
    return item['name']
def get_name(item):
    return item['age']
def get_name(item):
    return item['class']

by_name = sorted(l, key=get_name)
print(by_name)






