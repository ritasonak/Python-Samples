from itertools import islice, count
from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

# islice and count sample


thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
lst = list(thousand_primes)
print lst
sum_thousand_primes = sum(lst)
print(sum_thousand_primes)

# all and any sample


prime_exists = any(is_prime(x) for x in range(1328, 1361))
print prime_exists

title_case_exists = all(name == name.title() for name in ["Banglore", "Mumbai", "Delhi"])
print title_case_exists


# zip sample

sunday = [10, 11, 12, 13, 14, 15, 16, 17]
monday = [18, 19, 20, 21, 22, 23, 24, 25]
tuesday = [11, 21, 31, 41, 51, 61, 71, 81]
for item in zip(sunday, monday):
    print(item)

for sun, mon in zip(sunday, monday):
    print ("average=", sun+mon/2)
for temps in zip(sunday, monday, tuesday):
    print("min={:4.1f}, max={:4.1f}".format(min(temps), max(temps)))

