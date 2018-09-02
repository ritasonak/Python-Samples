m = [9, 15, 24]
f = [4, 5, 6]


def modify(k):
    k.append(39)
    print("k=", k)


def replace(g):
    g = [1, 2, 3]
    print("g=", g)


if __name__ == "__main__":
    # modify(m)
    replace(f)
# print m
print f
