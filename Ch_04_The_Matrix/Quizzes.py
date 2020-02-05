import sys
sys.path.insert(0, "../lib")
from vec import Vec

# Quiz 4.1.1: Write a nested comprehension whose value is list-of-row-list representation of a
# 3 × 4 matrix all of whose elements are zero
print([[0 for j in range(4)] for i in range(3)])

# Quiz 4.1.2: Write a nested comprehension whose value is list-of-column-lists representation of
# a 3 × 4 matrix whose i, j element is i − j
print([[i-j for i in range(3)] for j in range(4)])

# Quiz 4.1.5: Give a Python expression whose value is the coldict representation of the matrix
# of Example 4.1.3 (Page 187).
D = {'a', 'b'}
col_1 = Vec(D, {'a':1, 'b':10})
col_2 = Vec(D, {'a':2, 'b':20})
col_3 = Vec(D, {'a':3, 'b':30})
coldict = {'@':col_1, '#':col_2, '?':col_3}
print(coldict)
