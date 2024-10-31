# dump(), dumps()

import json
a = {"hai": 3, "hello": 4}

b = json.dumps(a)   # Serialize any python object into json format file
print(b)
print(type(b))      # str

c = json.loads(b)    # Deserialize any json string to python object'''
print(c)
print(type(c))      # dict


# =======================================================
a = True
print(type(a))

b = json.dumps(a)
print(b)
print(type(b))

# =========================================================

a = {"a": 1, "b": 2, "c": 3}

with open("sample.json", "a") as file:
    print(json.dump(a, file))      # Serialize any python object into json format file

with open("sample.json") as file:
    print(json.load(file))      # Deserilize any json object to python object'''
