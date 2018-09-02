
# find length of string
print len("sdfjgdsjfgfjdsgdf fgdfgdflgdfh dfghlkfghk")

# concatenation
print("New" + "found" + "land")

sample = ''.join(["high", "way", "man"])
print sample

sample = ";".join(["high", "way", "man"])
print sample

# split basis a delimiter
lst = sample.split(";")
print lst

#partition
print "unforgetable".partition("forget")

departure, seperator, arrival = "London:Edinburg".partition(":")
print(departure)
print(arrival)

#formatting a string
print "The age of {0} is {1}".format("Jim", 32)

print "The age of {} is {}".format("Jim", 32)

print "The age of {name} is {age}".format(name="Jim", age=32)

lst = ("Jim",32)
print "The age of {lst[0]} is {lst[1]}"



