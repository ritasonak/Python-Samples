def minmax(items):
    return min(items), max(items)

# defining a tuple
t = ("India", 1, 2.0)
print t
print[0]

# find length of a tuple
print "length of t-" + str(len(t))

# nested tuple
a = ((2, 3), (6, 7), (8, 9))
print a[0]
print a[0][0]

# returning multiple values from function using tuple
p = 1, 2, 3, 4, 5, 6, 19
print minmax(p)

#unpacking tuple
lower, upper = minmax([1, 2, 34])
print lower
print upper


(a, b, (c, d), e) = (1, 3, (4, 5), 6)
print a
print b
print c
print d

print 5 in (1, 2, 3, 4)

print 5 not in (1, 2, 3, 4)
