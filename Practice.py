import pickle

# Sample Python object (in this case, a dictionary)
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Pickle (serialize) the object into a binary file
with open('data.pkl', 'wb') as pickle_file:
    p = pickle.dump(data, pickle_file)
print(p)
















