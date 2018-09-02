from pprint import pprint as pp
import os
import glob
from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


words = "My name is Rita. I am a very good developer".split()
print words
# List Comprehension
len_list = [len(word) for word in words]
print len_list


# Set Comprehension
len_set = {len(word) for word in words}
print len_set


# Dictionary Comprehension
country_to_capital = {"UK": "London",
                      "Brazil": "Brazilia",
                      "Sweden": "Stockholm"}
capital_to_country = {capital: country for country, capital in country_to_capital.items()}
pp(capital_to_country)


# later Keys overwrite earlier keys sample
words = ["hi", "bye", "tye", "hello"]
dict = {x[0]: x for x in words}
print dict


# complex dict comprehension
file_sizes = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob("*.py")}
pp(file_sizes)

# Filtering Predicates
prime_list = [x for x in range(101) if is_prime(x)]
print prime_list