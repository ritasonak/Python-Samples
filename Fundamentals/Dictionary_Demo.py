urls = {"Google": "www.google.com",
        "Yahoo": "www.yahoo.com",
        "MSN": "www.msn.com"}
print urls["MSN"]

# creating dictionary with dict()
name_ages = [("Alice", 32), ("Bob", 28), ("Charlie", 20)]
d = dict(name_ages)
print (d)

e = dict(Alice=32, Bob=28, Charlie=20)
print e

# extend dictionary
f = dict(Daniel=23, Karla=10)
e.update(f)
print e

# iteration is over keys
for key in e:
    print("Name-{0}, Age-{1}".format(key, e[key]))

# iterating over values
for value in e.values():
    print value

# iterating over key, value
for key, value in e.items():
    print("Key-{0}, Value-{1}".format(key, value))

#delete an item
del e['Karla']
print e

#add an item
e["Karla"]= 10
print e