import sys
sys.path.insert(0, "../lib")

from vec import Vec

# Example 3.1.6: Products and resources:

D = {'metal','concrete','plastic','water','electricity'}
v_gnome = Vec(D,{'concrete':1.3,'plastic':.2,'water':.8,'electricity':.4})
v_hoop = Vec(D, {'plastic':1.5, 'water':.4, 'electricity':.3})
v_slinky = Vec(D, {'metal':.25, 'water':.2, 'electricity':.7})
v_putty = Vec(D, {'plastic':.3, 'water':.7, 'electricity':.5})
v_shooter = Vec(D, {'metal':.15, 'plastic':.5, 'water':.4,'electricity':.8})

print(240*v_gnome + 55*v_hoop + 150*v_slinky + 133*v_putty + 90*v_shooter)

# Quiz 3.1.7: Define a procedure lin_comb(vlist, clist) with the following spec:
# • input: a list vlist of vectors, a list clist of the same length consisting of scalars
# • output: the vector that is the linear combination of the vectors in vlist with corresponding
# coefficients clist
def lin_comb(vlist, clist):
	result_vec = Vec(D, {})
	for vec, a in zip(vlist, clist):
		result_vec = result_vec + (a * vec)
	return result_vec

quantities = [240, 55, 150, 133, 90]

products = [
 	Vec(D,{'concrete':1.3,'plastic':.2,'water':.8,'electricity':.4}),
 	Vec(D, {'plastic':1.5, 'water':.4, 'electricity':.3}),
 	Vec(D, {'metal':.25, 'water':.2, 'electricity':.7}),
 	Vec(D, {'plastic':.3, 'water':.7, 'electricity':.5}),
 	Vec(D, {'metal':.15, 'plastic':.5, 'water':.4,'electricity':.8})
]

b = lin_comb(products, quantities)
print(b)

# Computational Problem 3.1.8: Expressing a given vector as a linear combination of other
# given vectors
# • input: a vector b and a list [v1, . . . , vn] of n vectors
# • output: a list [α1, . . . ,αn] of coefficients such that
# b = α1 v1 + · · · + αn vn
# or a report that none exists.
def linearcomb_to_coefficients(b, vlist):
	result_vec = Vec(D, {})
	for vec, comb in zip(vlist, b):
		result_vec = result_vec + (comb * vec)
	return result_vec

print(linearcomb_to_coefficients(b, products))