import sys
sys.path.insert(0, "../lib")
from vec import Vec
from vecutil import zero_vec

""" Problem 3.8.1: """

# 1. Write and test a procedure vec_select using a comprehension for the following 
# computational problem:
# • input: a list veclist of vectors over the same domain, and an element k of the
# domain
# • output: the sublist of veclist consisting of the vectors v in veclist where v[k] is
# zero
def vec_select(veclist, k):
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select([v1, v2, v3, v4], 'a') == [Vec(D,{'b': 1}), Vec(D,{'b': 2})]
    True
    '''
    V_L = [ v for v in veclist if v[k]==0]
    for v in V_L:
        v.f = { x:y for (x,y) in v.f.items() if x!=k }
    return V_L
	
# 2. Write and test a procedure vec sum using the built-in procedure sum(·) for the following:
# • input: a list veclist of vectors, and a set D that is the common domain of these
# vectors
# • output: the vector sum of the vectors in veclist.
def vec_sum(veclist, D):
	'''
	>>> D = {'a', 'b', 'c'}
	>>> veclist = [ Vec(D, {'a':10, 'b':20, 'c':30}), Vec(D, {'a':5,  'b':12, 'c':19}), Vec(D, {'a':11, 'b':22, 'c':33}) ]
	>>> vec_sum(veclist, D) == Vec(D, {'a':26, 'b':54, 'c':82})
	True
	'''
	vector_sum = zero_vec(D)
	for d in D:
		vector_sum[d] = sum([v[d] for v in veclist]) 
	return  vector_sum

# 3. Put your procedures together to obtain a procedure vec select sum for the following:
# • input: a set D, a list veclist of vectors with domain D, and an element k of the
# domain
# • output: the sum of all vectors v in veclist where v[k] is zero
def vec_select_sum(veclist, D, k):
	'''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2, 'c':10})
    >>> v4 = Vec(D, {'a': 10,'b':10})
    >>> vec_select_sum([v1, v2, v3, v4], D, 'a') == Vec(D,{'a': 0, 'b':3, 'c':10})
    True
    '''
	return vec_sum(vec_select(veclist, k), D)

# Problem 3.8.2: Write and test a procedure scale vecs(vecdict) for the following:
# • input: A dictionary vecdict mapping positive numbers to vectors (instances of Vec)
# • output: a list of vectors, one for each item in vecdict. If vecdict contains a key k
# mapping to a vector v, the output should contain the vector (1/k)v
def scale_vecs(vecdict):
	'''
	>>> D = {1, 2, 3, 4}
	>>> v1 = Vec(D, {1:10, 2:20, 3:30, 4:40})
	>>> v2 = Vec(D, {1:12, 2:22, 3:32, 4:42})
	>>> v3 = Vec(D, {1:18, 2:24, 3:30, 4:48})
	>>> v4 = Vec(D, {1:5.0, 2:10.0, 3:15.0, 4:20.0})
	>>> v5 = Vec(D, {1:3.0, 2: 5.5, 3: 8.0, 4:10.5})
	>>> v6 = Vec(D, {1:3.0, 2: 4.0, 3: 5.0, 4: 8.0})
	>>> scale_vecs({2:v1, 4:v2, 6:v3}) == [v4, v5, v6]
	True
	'''
	veclist = []
	for k,vec in vecdict.items():
		veclist.append((1/k)*vec)
	return veclist

# Problem 3.8.3: Write a procedure GF2_span with the following spec:
# • input: a set D of labels and a list L of vectors over GF(2) with label-set D
# • output: the list of all linear combinations of the vectors in L
# (Hint: use a loop (or recursion) and a comprehension. Be sure to test your procedure on examples
# where L is an empty list.)
