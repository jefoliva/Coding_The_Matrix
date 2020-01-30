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
	return vector_sum
D = {'a', 'b', 'c'}
veclist = [
	Vec(D, {'a':10, 'b':20, 'c':30}),
	Vec(D, {'a':5,  'b':12, 'c':19}),
	Vec(D, {'a':11, 'b':22, 'c':33})
]