# Use Numpy to make/play with arrays

import numpy as np

# make random 5x5 array and print it
array = np.random.randint(0, 9, size=(5, 5), dtype=int)
print(array)

# print second row third column
print(array[1, 2])

# print sum of full array
total = np.sum(array)
print(total)
