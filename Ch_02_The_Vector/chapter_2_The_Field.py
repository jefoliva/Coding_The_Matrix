import sys
sys.path.insert(0, "../lib")

from math import e
from math import pi
from plotting import plot
from image import file2image

# imaginary number sqrt(-1) = 1i
# complex number: The sum of a real number with an imaginary number
# ex. 3+3j


x = 1 + 3j
print((x-1)**2)		# -9 + 0j

# Get real or imagnary part using dot notation
print(x.real)	# 1.0 
print(x.imag)	# 3.0
type(1+2j)		# complex
def solve(a, b, c): return (c-b/a)
print(solve(10+5j, 5, 20))

import sys
sys.path.insert(1, '')

S = {2 + 2j,3 + 2j, 1.75 + 1j,2 + 1j, 2.25 +
1j, 2.5 + 1j, 2.75 + 1j,3 + 1j, 3.25 + 1j}

# plot(S, 4)

# The absolute of a complex number is the distantce from the origin to the
# corresponding point in the complex plane
print( abs(3+4j) )

# The conjugate of a complex number is defined as z.real - z.imag
print( (3+4j).conjugate() )

# Shift each point in S, 1 unit to the right and 2 up
S = {1+2j+z for z in S}
# plot(S, 4)
point = {2+2j}
# plot({x-2-2j for x in point}, 4)

# MULTIPLYING COMPLEX NUMBERS BY A POSITIVE REAL NUMBER
S = {2 + 2j,3 + 2j, 1.75 + 1j,2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j,3 + 1j, 
	3.25 + 1j}

my_scaled_points = {0.5*z for z in S}
# plot(my_scaled_points, 4)

# Rotation by 180 degrees.
# Multiply by -1
rot_180_deg = {-1*z for z in S}
# plot(rot_180_deg|S, 4)


# ROTAING BY 90 DEGREES
# a point located at (x,y) must be moved to  (-y,x) the complex number located
# at(x,y) is x + iy. Multiplying by i yields ix + i^2y, which is ix-y
# which is the complex number represented by the point (-y, x) 
rot_90_deg = {1j*z for z in S}
# plot(rot_180_deg|rot_90_deg, 4)

# Task 1.4.9: Using a compr(ehension, create a new plot in which the points of S are rotated by
# 90 degrees, scaled by 1/2, and then shifted down by one unit and to the right two units. Use
# a comprehension in which the points of S are multiplied by one complex number and added to
# another.
T = { 1j*z * 0.5 + 2-1j for z in S}
# plot(T|S,4)

# Task 1.4.10:
data = file2image('../Material/img01.png')
# print(data)
height = len(data)
width =len(data[0])
pts=[x+(189j+y*-1j) for x in range(width) for y in range(height) if data[y][x][0]<120]
print(len(pts))
# points = {x+(y*-1j) for x in range(len(data)) for y in range(len(data[0])) if data[x][y][0] < 120}
# print(points)``
# points_rot = {-1j*x for x in points}
# plot(points, 200, 1)
# plot(set(points|points_rot), 200, 1)

# Task 1.4.11: Write a Python procedure f(z) that takes as argument a complex number z so
# that when f(z) is applied to each of the complex numbers in S, the set of resulting numbers
# is centered at the origin.
# def center_at_origin(S):
# 	S_center_x = s.le

# Task 1.4.17: From the module math, import the definitions e and pi. Let n be the integer
# 20. Let w be the complex number e2πi/n. Write a comprehension yielding the list consisting of
# w0, w1, w2, . . . ,wn−1. Plot these complex numbers.
l = [e**(2*pi*(1j/n)) for n in range(20) if n != 0]
# plot(l, 4, 1)

# Task 1.4.18: Recall from Task 1.4.1 the set S of complex numbers. Write a comprehension
# whose value is the set consisting of rotations by π/4 of the elements of S. Plot the value of this
# comprehension.
S = {2 + 2j,3 + 2j, 1.75 + 1j,2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j,3 + 1j, 3.25 + 1j}
T = {Z*e**(pi/4*1j) for Z in S}
# plot(T|S, 4, 1)
# pi_pts = {Z*e**(pi/4*1j) for Z in pts}
# plot(pi_pts, 300, 1)

# Task 1.4.20
pts2 = {x*.5*(e**(1j*pi/4))-55j for x in pts}
# plot(pts2, 300, 1)

# Problem 1.5.1: An 11-symbol message has been encrypted as follows. Each symbol is represented
# by a number between 0 and 26 (A )→ 0,B )→ 1, . . . ,Z )→ 25, space )→ 26). Each number
# is represented by a five-bit binary sequence (0 )→ 00000, 1 )→ 00001, ..., 26 )→ 11010). Finally,
# the resulting sequence of 55 bits is encrypted using a flawed version of the one-time pad: the
# key is not 55 random bits but 11 copies of the same sequence of 5 random bits. The cyphertext
# is
# 10101 00100 10101 01011 11001 00011 01011 10101 00100 11001 11010
# Try to find the plaintext.

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']

decrypt_dict = { "{0:05b}".format(x):(x, y) for x in range(len(alphabet)) for y in alphabet[x]}
# print(system)

enc_msg = ['10101', '00100', '10101', '01011', '11001', '00011', '01011', '10101', '00100', '11001', '11010']
keys = [k for k in decrypt_dict.keys()]

ans = ''
kel = []
def decrypt(k, c):
    m = []
    for key in keys:
        for bit in enc_msg:
            el = ''
            for i in range(len(bit)):
                el = el + str(int(key[i]) ^ int(bit[i]))
            m.append(el)
            kel.append(key)
    return m;

decrypt_msg = decrypt(keys, enc_msg)

# for i in range(len(decrypt_msg)):
#     bit = decrypt_msg[i]
#     if bit in decrypt_dict:
#         print(str(i) + ' ' + bit + ' ' + decrypt_dict[bit][1])

#     if (i % 11) == 0 and i != 0:
#         print('\n\n')

# # print(ans)
# # print(list(enumerate(kel)))

# thekey = '10001'
# msg = [x for (x,y) in list(enumerate(kel)) if x > 186 and x < 198]
# print(msg)
# m = []
# for bit in enc_msg:
#     el = ''
#     for i in range(len(bit)):
#         el = el + str(int(thekey[i]) ^ int(bit[i]))
#     m.append(el)
# print(m)

# for el in m:
#     print(decrypt_dict[el][1])


# PROBLEMS


# Problem 1.7.1: my filter(L, num)
# input: list of numbers and a positive integer.
# output: list of numbers not containing a multiple of num.
# example: given list = [1,2,4,5,7] and num = 2, return [1,5,7].

def my_filter(L, num):
    output = [x for x in L if (x % num) != 0]
    return output

print( my_filter([1,2,4,5,7], 2) )

# Problem 1.7.4: mySum(L)
def mySum(L):
    current = 0;
    for x in L:
        current += x;
    return current

# print(mySum([1, 2, 3, 4]))
# print(mySum([1, 2, 3, 4]))

# Task 2.4.3: Recall the list L defined in Task 2.3.2. Enter the procedure definition for 2-vector
# addition, and use a comprehension to plot the points obtained from L by adding [1, 2] to each:
# >>> plot([add2(v, [1,2]) for v in L], 4)
L = [[2, 2], [3, 2], [1.75, 1], [2, 1], [2.25, 1], [2.5, 1], [2.75,
1], [3, 1], [3.25, 1]]

def add(u, v):
    return [x+y for x,y in zip(u,v)]

print([add(v, [1,2]) for v in L])
# plot([add(v, [1,2]) for v in L], 5, 1)

# Quiz 2.5.3: Suppose we represent n-vectors by n-element lists. Write a procedure
# scalar_vector_mult(alpha, v) that multiplies the vector v by the scalar alpha.
def scalar_vector_mult(alpha, v):
    return [x*alpha for x in v]

print(scalar_vector_mult(3, [2, 3, 4, 5, 6]))

# Task 2.5.4: Plot the result of scaling the vectors in L by 0.5, then plot
# the result of scaling them by -0.5.
M = [scalar_vector_mult(0.5, v) for v in L]
N = [scalar_vector_mult(-0.5, v) for v in L]

print()
# plot(.extend(), 5, 1)

# Line segments through the origin.
v = [3, 2]
print([scalar_vector_mult(i/10, v) for i in range (11)])
# plot([scalar_vector_mult(i/10, v) for i in range (11)], 5)

# drow line segment
# plot([add(scalar_vector_mult(i/100., [3,2]), [0.5,1]) for i in range(101)], 4, 2)

# Task 2.6.9: Write a python procedure segment(pt1, pt2) that, given points represented as
# 2-element lists, returns a list of a hundred points spaced evenly along the line segment whose
# endpoints are the two points
# Plot the hundred points resulting when pt1 = [3.5, 3] and pt2 = [0.5, 1]

p1 = [0,0] 
p2 = [100, 140]

def segment(pt1, pt2):
    ranges = [x/100 for x in [y for y in range(0, 100)]]
    points = [add(scalar_vector_mult(1-n, p1), scalar_vector_mult(n, p2)) for n in ranges]
    return points

# plot(segment(p1, p2), 150, 1)


# VECTOR CLASS
class Vec:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

def setitem(v, d, value):
    v.f[d] = value

def getitem(v, d):
    if d in v.f:
        return v.f[d]
    else:
        return 0

def scalar_mul(v, alpha):
    return Vec(v.D, {d:alpha*value for d,value in v.f.items()})

def add(u, v):
    return Vec(u.D,{d:getitem(u,d)+getitem(v,d) for d in u.f.keys()})


v = Vec({'A', 'B', 'C'}, {'A':1})
u = scalar_mul(v, 3)
w = add(u, v)
for d in u.f:
    print(u.f[d])


# Quiz 2.7.5: Write a Python procedure neg(v) with the following spec:
# • input: an instance v of Vec
# • output: a dictionary representing the negative of v
def neg(v):
    return Vec(v.D, {k:-v for k, v in v.f.items()})

# Quiz 2.9.4: Write a procedure list_dot(u, v) with the following spec:
# • input: equal-length lists u and v of field elements
# • output: the dot-product of u and v interpreted as vectors
# Use the sum(·) procedure together with a list comprehension.
def list_dot(u, v):
    return sum([a*b for a,b in zip(u, v)])

print(list_dot([1,0.5,0.5,1], [0, 0, 1.0, 1.0]))


# FINDING AN AUDIO CLIP
# Quiz 2.9.15: Write a procedure dot_product_list(needle,haystack) with the following
# spec:
# • input: a short list needle and a long list haystack, both containing numbers
# • output: a list of length len(haystack)-len(needle) such that entry i of the output list
# equals the dot-product of the needle with the equal-length sublist of haystack starting at
# position i
# Your procedure should use a comprehension and use the procedure list_dot(u,v) from Quiz 2.9.4.
# Hint: you can use slices as described in Section 0.5.5.
def dot_product_list(needle, haystack):
    s = len(needle)
    return [list_dot(needle, haystack[i:i+s]) for i in range(len(haystack)-s)]

print(dot_product_list([1,2,3], [1,2,3,4,5,6,7,8]))


# Quiz 2.10.1: Write a procedure list2vec(L) with the following spec:
# • input: a list L of field elements
# • output: an instance v of Vec with domain {0, 1, 2, . . . , len(L) − 1} such that v[i] = L[i]
# for each integer i in the domain
def list2vec(L):
    return Vec({i for i in range(len(L))}, {k:v for k, v in enumerate(L)})

print(list2vec([2,4,6,8,10]).f)

def zero_vec(D): return Vec(D, {})

def triangular_solve_n(rowlist, b):
    D = rowlist[0].D
    n = len(D)
    # print(D)
    # print(n)
    # print(set(range(n)))
    assert D == set(range(n))
    x = zero_vec(D)
    for i in reversed(range(n)):
        x[i] = (b[i] - rowlist[i] * x)/rowlist[i][i]
    return x

# Exercise 2.11.4: Enter triangular_solve_n into Python and try it out on the example
# system above.
D = {0, 1, 2}

veclist = [
    Vec(D, {0:2, 1:2, 2:4}),
    Vec(D, {1:1, 2:2}),
    Vec(D, {2:5})
] 

b = [10, 3, 5]

print(triangular_solve_n(veclist, b))