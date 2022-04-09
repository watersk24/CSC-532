# Student name(s): Kevin Waters

# Mini Universal Hashing
# The class definition below is a HashTable with a built-in hash function.
# The built-in hash function used the division method (see the textbook or the lecture notes).
# Let's add two more hash functions first:
#   - Multiplication Method with the constant A suggested by Knuth
#   - Universal class of hash function:((ak + b) mod p) mod m    (equation 11.3 in the textbook)
#       - k as a new key
#       - m as the size of the hash table (self.size)
#       - p as 127, a as 3, b as 5 (you can hard-code those values)

# After having three different hash functions, please make them a list (yes, I mean a list of functions)
# Next, change the constructor:
#   - create a new instance variable called "random_seed".
#   - it is initialized to be a random value of 0, 1, or 2 (because we only have 3 possible hash functions
#       - random package has been imported, you should use random.randint()
#       - see documentation here: https://docs.python.org/3.7/library/random.html
#   - print the random_seed after it is picked randomly
#   - once the random_seed is created, the hash table should use it **consistently** for adding/search values

import math
import random
import time


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.hashfunctions = [self.hashfunction, self.hash_multiply, self.universal_hash]
        self.random_seed = random.randint(0, 2)
        print("Algorithm: ", self.hashfunctions[self.random_seed].__name__)
        print("Random seed: ", self.random_seed)

    def put(self, key, data):
        start = time.time()
        number_of_inserts = 0
        hash_function = self.hashfunctions[self.random_seed]
        algorithm = hash_function.__name__
        hashvalue = hash_function(key, len(self.slots))
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and \
                                self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace
        stop = time.time()
        number_of_inserts += 1
        insert_time = str(stop - start)

        return insert_time, number_of_inserts, algorithm

    def hashfunction(self, key, size):
        return key % size

    def hash_multiply(self, key, size):
        #  h(k) = floor(m(k * A % 1))
        A = random.uniform(0, 1)  # for 0 < A < 1
        a = (key * A) % 1
        return math.floor(size * a)

    def universal_hash(self, key, size):
        #  universal hash function = ((ak + b) mod p) mod m
        p = 127
        a = 3
        b = 5
        return (((a * key) + b) % p) % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        hash_function = self.hashfunctions[self.random_seed]
        startslot = hash_function(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

H = HashTable()
d = {54: "cat", 26: " dog", 93: " lion", 17: "tiger", 77: 'bird', 31: 'cow', 44: 'goat', 55: 'pig', 20: 'chicken'}

H[54] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"

print('H.slots: ', H.slots)
print('H.data', H.data)
print("H[31]=", H[31])  #H[31]= cow
print("H[44]=", H[44])  #H[44]= goat
print("H[55]=", H[55])  #H[55]= pig
print("H[56]=", H[56])  #H[56]= None
print("H.slots: ", H.slots)
#Below is a sample output when universal hashing is used.
"""
Random Seed: 2
[31, 17, 44, 55, 20, None, 26, 54, 93, None, 77]
['cow', 'tiger', 'goat', 'pig', 'chicken', None, 'dog', 'cat', 'lion', None, 'bird']
H[31]= cow
H[44]= goat
H[55]= pig
H[56]= None
"""