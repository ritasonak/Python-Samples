s = "show how to index into sequence".split()
print s

print s[0]

print s[-1]

# slicing
print s[-3: -1]

print s[1:-1]

print s[3:]

print s[-3:]

# Copy Methods
full_slice = s[:]
print(full_slice)

u = list(s)
print u

# finding an element
w = "the quick brown fox jumps over the lazy dog".split()
print w.index("dog")

print w.count("dog")

# removing element from the list
u = "jackdaw love my big sphinx of quartz".split()
del u[2]
print u

u.remove("jackdaw")
print u

# adding element to list
a = "I accidentally the whole universe".split()
a.insert(2, "destroyed")
print a

# concatenating list
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = b + a
print c
c += [811]
print c
c.extend([12, 13])
print c

# reverse/sort
c.reverse()
print c
c.sort()
print c
d = reversed(c)
print d
e = sorted(d)


