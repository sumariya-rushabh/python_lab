#Example 1: Basic slices
"""
from array import array
arr = array('i', [10, 20, 30, 40, 50])
print(arr[1:4])  # Output: array('i', [20, 30, 40])
print(arr[:3])   # Output: array('i', [10, 20, 30])
print(arr[2:])  # Output: array('i', [30, 40, 50])
print(arr[:])   # Output: array('i', [10, 20, 30, 40, 50])


#Example 2: Slices with step

from array import array
arr = array('i', [10, 20, 30, 40, 50])
print(arr[::2])  # Output: array('i', [10, 30, 50])
print(arr[1::2]) # Output: array('i', [20, 40])
print(arr[::3]) # Output: array('i', [10, 40])


#Example 3: Negative indexing with slices

from array import array
arr = array('i', [10, 20, 30, 40, 50])
print(arr[-4:-1])  # Output: array('i', [20, 30, 40])
print(arr[-3:])    # Output: array('i', [30, 40, 50])
print(arr[:-2])    # Output: array('i', [10, 20, 30])


#Example 4: Reverse array using slicing
from array import array
arr = array('i', [10, 20, 30, 40, 50])
reversed_arr = arr[::-1]
print(reversed_arr)  # Output: array('i', [50, 40, 30, 20, 10])
"""