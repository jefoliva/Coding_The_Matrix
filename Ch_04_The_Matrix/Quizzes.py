import sys
sys.path.insert(0, "../lib")
from vec import Vec
from mat import Mat

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

# Quiz 4.1.7: Write an expression for the {'a','b','c'}×{'a','b','c'} identity matrix represented
# as an instance of Mat.
m = Mat(({'a', 'b', 'c'}, {'a', 'b', 'c'}), {('a', 'a'):1, ('b', 'b'):1, ('c', 'c'):1})
print(m.f)

def identity(D):
	m = Mat((D,D), {(d,d):1 for d in D})
	return m.f

print(identity({'a', 'b'}))

# Quiz 4.1.9: Write a one-line procedure mat2rowdict(A) that, given an instance 
# of Mat, returns the rowdict representation of the same matrix. Use dictionary 
# comprehensions.
# test
def mat2rowdict(A):
	return {r:Vec(A.D[1],{c:A.f[r,c] for c in A.D[1]}) for r in A.D[0]}

D = ({'a', 'b'},{'@', '#', '?'})
m = Mat(D, {('a', '@'):1, ('a', '#'):2, ('a','?'):3, ('b','@'):10, ('b','#'):20, ('b','?'):30})
# print(mat2rowdict(m))

# Quiz 4.1.10: Write a one-line procedure mat2coldict(A) that, given an instance of Mat,
# returns the coldict representation of the same matrix. Use dictionary comprehensions.
def mat2coldict(A):
	return {c:Vec( A.D[0], { r:A.f[r,c] for r in A.D[0]} ) for c in A.D[1] }

print(mat2coldict(m))

# Quiz 4.3.1: Write the procedure mat2vec(M) that, given an instance of Mat, returns the corresponding
# instance of Vec. As an example, we show the result of applying this procedure to the
# matrix M given in Example 4.1.3 (Page 187):
def mat2vec(M):
	return Vec({(r, c) for r in M.D[0] for c in M.D[1]}, M.f)  

print(mat2vec(m))
	