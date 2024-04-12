#Slicing on one dimensional ndarray is the same as in python list.The difference is that the slice is not a copy but rather a view ofthe original array

#In multi dimensional arrays slicing needs to take more parameters, just like indexing:

#1
import random
import time
import numpy as np

N = 10**8
a = []
# list of 10 million numbers
for _ in range(N):
  a.append(random.randint(1, N))

start = time.perf_counter()
a.sort()
end = time.perf_counter()
print(f"classic took {end-start}")

a = np.random.randint(1, N, N)
start = time.perf_counter()
a.sort()
end = time.perf_counter()
print(f"NumPy took {end-start}")

#2

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a)
print(a[1:5])
slice = a[1:5]
slice[0] = 35

print(a)
slice[:] = 35 # careful here with slice = 35
print(a)
print("\n\n")


a = np.arange(12)
a = a.reshape((3, 4))
print(f"a=\n{a}")
print(f"a[:, 1]=\n{a[:, 1]}")
print(f"a[:2, :2]=\n{a[:2, :2]}")
a[:2, :2] = 99
print(f"a=\n{a}")

#Boolean Indexing
#Boolean operation can be applied to ndarrays and will produce a True/False ndarray.
# This arrays can be used to index other arrays as long as they have the same size:

names = np.array(["Bob", "James", "Mary", "Bob", "Jane", "Bob", "James", "Jane"])
print(names == "Bob")
a = np.arange(24).reshape((8, 3))
print(f"a=\n{a}")
print(f"a[names == 'Bob']=\n {a[names == 'Bob']}")
a[names=="Jane", :2 ] = 99
print(f"a=\n{a}")

#You can string multiple conditions using the| (or) and & (and) operator. Be advised that and, or do not work on ndarrays
print(f"{a[(names == 'Bob') | (names=='Jane')]}")
#Selecting data from an array by boolean indexing and assigning the result to a new variable always creates a copy of the data, even if the returned array is unchanged.
a = np.zeros((8, 3), dtype=np.int16)
for i in range(8):
  a[i] = i



#FANCY INDEXING
#Fancy indexing is the indexing of numpy ndarrays using integer arrays:
print(a)
fancy_index = [1, 3, 5]
print(f"a[fancy] = \n{a[fancy_index]}")

#Negative indices selects from the end:

fancy_index2 = [-1, -2, -4]
print(f"a[fancy2] = \n{a[fancy_index2]}")

#Passing multiple arrays will select based on the tuple indices of the arrays provided:

a = np.arange(24).reshape((8, 3))
print(f"a=\n{a}")
fancy1 = [0, 2, 4, 7]
fancy2 = [0, 0, 1, 0]
print(f"a[fancy_fancy] = \n{a[fancy1, fancy2]}")
