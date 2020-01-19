s = {1, 2, 3}

# Comprehension
t = {2*x for x in s}
print(t)

# Task 0.5.5: Write a comprehension over {1, 2, 3, 4, 5} whose value is the set consisting of
# the squares of the first five positive integers.
t = {x**2 for x in {1,2,3,4,5}}
print(t)

# Task 0.5.6: Write a comprehension over {0, 1, 2, 3, 4} whose value is the set consisting of
# the first five powers of two, starting with 2^0.
t = {2**x for x in {0, 1, 2, 3, 4}}
print(t)

S = {1, 3}
print({x*x for x in S | {5,7}})

# LISTS

L = [20, 10, 15, 75]
M = [[1,2], [3,4], [5,6]]

print(sum(L)/len(L))

# print(sum(M))		# Error
print(sum(M, []))	# Correct

# List comprehension
print( [2*x for x in {2, 1, 3, 4, 5}] )

# double comprehension
print( [x*y for x in {1, 2, 3} for y in {10, 20, 30}] )

# Task 0.5.11: Write a double list comprehension over the lists ['A','B','C'] and [1,2,3]
# whose value is the list of all possible two-element lists [letter, number].
print( [ [x, y] for x in ['A', 'B', 'C'] for y in [1, 2, 3] ] )

# SLICES
mylist = [1, 2, 3, 5, 8, 13]
print(mylist[2:5])

# Prefix
print(mylist[:5])

# sufix
print(mylist[4:])

# slice with step
L = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(L[::2])	# even indexed elements
print(L[1::2])	# odd indexed elemennts

# unpacking
mylist = [[1,2,3], [4,5,6], [7,8,9]]

print([z for [x,y,z] in mylist])

# Tuples 
# Tuples are like lists, but immutable, so they can be elements of sets
mytuple = (1, 2, 3)
print(mytuple)

print({0, 1, (1, 2)} | {(3,4,5)})

# tuples with unpacking
print( [y for (x, y) in [(1, 'A'), (2, 'B'), (3, 'C')] ] )

# Task 0.5.14: Suppose S is a set of integers, e.g. {−4,−2, 1, 2, 5, 0}. Write a triple
# comprehension whose value is a list of all three-element tuples (i, j, k) such that i, j, k are
# elements of S whose sum is zero.
Set = {-4,-2, 1, 2, 5, 0}
print([ (x,y,z) for x in Set for y in Set for z in Set if x + y + z == 0 and (x!=0 and y !=0 and z != 0)])
print([ (x,y,z) for x in Set for y in Set for z in Set if x + y + z == 0 and (x,y,z) != (0,0,0)[0]])


# Obtaining a list or set from another collection

# list to set
print(set([2, 2, 3, 2 , 3, 4, 5]) )
print(list({2, 3 ,4 ,5 ,6 ,7 ,8}))

# Task 0.5.17: Find an example of a list L such that len(L) and len(list(set(L))) are
# different.
L = [1, 2, 2, 3, 4, 6]
print( len(L) ) 
print( len(list(set(L))) )

print( type( (i for i in [1,2,3]) ) )	 # generator


# RANGES
print( list(range(10)) ) # 0 to 9

# Task 0.5.18: Write a comprehension over a range of the form range(n) such that the
# value of the comprehension is the set of odd numbers from 1 to 99.
# print( [ x for x in list(range(100, 1, 2)) ] )
print( [x for x in range(100) if x % 2 != 0] )


# ZIP
# A collection contructed from other collection all of the same length
# each element is a tuple consisting of one element
# from each of the input collections.
print( list(zip([1,3,5], [2,4,6])) )

characters = ['Neo', 'Morpheus', 'Trinity']
actors = ['Keanu', 'Laurence', 'Carrie-Anne']

print( list(zip(characters, actors)) )

print( [characters + ' is played by ' + actors for (characters, actors) in zip(characters, actors)] )

# Task 0.5.19: Assign to L the list consisting of the first five letters ['A','B','C','D','E'].
# Next, use L in an expression whose value is
# [(0, ’A’), (1, ’B’), (2, ’C’), (3, ’D’), (4, ’E’)]
# Your expression should use a range and a zip, but should not use a comprehension.
L = ['A', 'B', 'C', 'D', 'E']
print( list(zip(list(range(5)), L)) )


# Task 0.5.20: Starting from the lists [10, 25, 40] and [1, 15, 20], write a comprehension
# whose value is the three-element list in which the first element is the sum of 10
# and 1, the second is the sum of 25 and 15, and the third is the sum of 40 and 20. Your
# expression should use zip but not list
A = [10, 25, 40]
B = [1, 15, 20]

# print( [x for x in A for Y in B for Z in zip(A, B, x+y) ] )
print( [sum(x) for x in zip(A, B)] )

# REVERSE
L = [4, 5, 10]
print(x for x in reversed(L))

# Dictionaries
# A set of key-value pairs

f = {'A':0, 'B':1, 'C':2 }
print(f['A'])

# if the key is not present, is considered an error
# print(f['D'])		# error

# Test dictionary memebeship
print('A' in f)
print('D' in f)

dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger',
'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]

print( [x['James'] for x in dlist] )

# Task 0.5.22: Modify the comprehension in Task 0.5.21 to handle the case in which k
# might not appear in all the dictionaries. The comprehension evaluates to the list whose ith
# element is the value corresponding to key k in the ith dictionary in dlist if that dictionary
# contains that key, and 'NOT PRESENT' otherwise.
# Test your comprehension with k = 'Bilbo' and k = 'Frodo' and with the following
# list of dictionaries:
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},
{'Bilbo':'Martin','Thorin':'Richard'}]

print( [x['Bilbo'] for x in dlist if 'Frodo' in x ])
print( [x['Frodo'] for x in dlist if 'Frodo' in x ])


# Mutate a dictionary
mydict = {'Agent Smith':'Boss'}
mydict['Agen Smith'] = 'Hugo'
mydict['Neo'] = 'Philip'

# Dictionary Comprehensions
mydict = {k:v for (k,v) in [(3,2), (4,0), (100,1)]}
print(mydict)

# Task 0.5.23: Using range, write a comprehension whose value is a dictionary. The keys
# should be the integers from 0 to 99 and the value corresponding to a key should be the
# square of the key.

D = {k:v for (k,v) in  zip(list(range(100)), [x**2 for x in range(100)] ) }
print(D)
print(D[5])

# Task 0.5.25: Using the variables base=10 and digits=set(range(base)), write a dictionary
# comprehension that maps each integer between zero and nine hundred ninety nine
# to the list of three digits that represents that integer in base 10.\
base = 10
baseDigits = list(range(base))

# basemapping = {k:v for (k,v) in zip(baseDigits, [] ) }

# Iterate over dictionaries

print( [2*x for x in {4:'a',3:'b'}.keys() ] )
print( [2*x for x in {4:'a',3:'b'}.values() ] )
print( [str(x)+ str(':') +str(y) for (x,y) in {4:'a',3:'b'}.items() ] )

id2salary = {0:1000.0, 3:990, 1:1200.50}
names = ['Larry', 'Curly', '', 'Moe']
print( {k:v for (k,v) in zip([x for x in names if x != ''], id2salary.values()) })


# DEFINING ONE LINE-PROCEDURES
def nextInt(list):
	return [x+1 for x in list]

print( nextInt([2, 4, 6]) )


def list2dict(L, keylist):
	return {k:v for (k,v) in zip(keylist, L)}

print( list2dict(['A', 'B', 'C', 'D'], ('a', 'b', 'c') ) )


# Importing modules
# import math
# help(math)

from random import randint
print(randint(3,10))



# reading from a file

f = open('Material/stories_small.txt')

# for line in f:
#     print(line)

f = open('Material/stories_small.txt')
stories = list(f)
print(len(stories))

# Mini-search engine

# enumerate()
print(list(enumerate(['A', 'B', 'C']))) 
print( [ str(i)+' '+str(item) for (i, item) in enumerate(['A', 'B', 'C']) ])
