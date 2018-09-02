import functools

# Procedural


def Doadd(list):
    sum = 0
    for x in list:
        sum += x
    return sum
mylist=[1, 2, 3, 4, 5]
print(Doadd(mylist))

# Object oriented programming
class ChangeList:
    def __init__(self, mylist):
        self._mylist=mylist
    def DoAdd(self):
        self.Sum=sum(self._mylist)


createSum = ChangeList(mylist=[1, 2, 3, 4, 5])
createSum.DoAdd()
print(createSum.Sum)

# Imperative
mylist = [1, 2, 3, 4, 5]
sum = 0
for x in mylist:
    sum += x
print sum

# Functional

mylist = [1, 2, 3, 4, 5]


def add(x, y):
    return x + y


sum = functools.reduce(add, mylist)
print(sum)




