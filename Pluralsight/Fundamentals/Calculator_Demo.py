import sys


def add(x, y):
    return x + y


def subtract(x, y):
    return x-y


if __name__== "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    print add(a, b)