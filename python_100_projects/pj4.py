"""
Sorting NumPy Arrays
There are a bunch of sorting algorithms in computer science, for example:

Insertion Sort
Selection Sort
Merge Sort
Bubble Sort and many more.
"""
import numpy
import numpy as np

a = np.array([34, 24, 69, 36, 78, 99])
print(numpy.sort(a))

def sorting(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x
print(sorting(a))
