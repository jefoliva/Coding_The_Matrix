import sys
sys.path.insert(0, "../lib")

from math import e
from math import pi
from plotting import plot
from image import file2image
from vec import Vec

v = Vec({'A', 'B', 'C'}, {'A':1})
print(v)
print(v[1])

def zero_vec(D): return Vec(D, {})

def triangular_solve_n(rowlist, b):
	D = rowlist[0].D
	n = len(D)
	assert D == set(range(n))
	x = zero_vec(D)
	for i in reversed(range(n)):
		x[i] = (b[i] - rowlist[i] * x)/rowlist[i][i]
	return x

D = {0, 1, 2, 3}

veclist = [
	Vec(D,{ 0:4, 1:-2, 2:0.5, 3:1}),
	Vec(D,{ 1:2, 2:3, 3:3}),
	Vec(D,{ 2:5, 3:1 }),
	Vec(D,{ 3:2})
] 

b = [6, -4, 3, -8]

print(triangular_solve_n(veclist, b))


def triangular_solve(rowlist, label_list, b):
	D = rowlist[0].D
	x = zero_vec(D)
	for j in reversed(range(len(D))):
		c = label_list[j]
		row = rowlist[j]
		x[c] = (b[j] - x*row)/row[c]
	return x

label_list = ['a','b','c','d']
D = set(label_list)
rowlist=[
	Vec(D,{'a':4, 'b':-2,'c':0.5,'d':1}), Vec(D,{'b':2,'c':3,'d':3}),
	Vec(D,{'c':5, 'd':1}), Vec(D,{'d':2.}) ]
b = [6, -4, 3, -8]

triangular_solve(rowlist, label_list, b)


# Lab: Comparing voting records using dot-product

# Task 2.12.1: Write a procedure create voting dict(strlist) that, given a list of
# strings (voting records from the source file), returns a dictionary that maps the last name
# of a senator to a list of numbers representing that senator’s voting record. You will need to
# use the built-in procedure int(·) to convert a string representation of an integer (e.g. ‘1’)
# to the actual integer (e.g. 1)

rootpath = '../Material/'

f = open(rootpath + 'voting_record_dump109.txt')
voting_file = list(f)

def create_voting_dict(strlist):
	senators_dict = {}
	for sen_votes in strlist:
		sen_votes = sen_votes.split(' ')
		sen_name = sen_votes[0]
		votes = []
		for vote in range(3, len(sen_votes)):
			votes.append(int(sen_votes[vote]))
		senators_dict[sen_name] = votes
	return senators_dict


senators_dict = create_voting_dict(voting_file)

print(senators_dict['Akaka'])
print(len(senators_dict['Akaka']))


# POLICY COMPARISON

# Task 2.12.2: Write a procedure policy compare(sen a, sen b, voting dict) that,
# given two names of senators and a dictionary mapping senator names to lists representing
# voting records, returns the dot-product representing the degree of similarity between two
# senators’ voting policies.

def policy_compare(sen_a, sen_b, voting_dict):
	result = 0
	for u,v in zip(voting_dict[sen_a], voting_dict[sen_b]):
		result += u * v
	return result


print(policy_compare('Akaka', 'Alexander', senators_dict))

# Task 2.12.3: Write a procedure most similar(sen, voting dict) that, given the name
# of a senator and a dictionary mapping senator names to lists representing voting records,
# returns the name of the senator whose political mindset is most like the input senator
# (excluding, of course, the input senator him/herself).
def most_similar(sen, voting_dict):
	VOTES = 46						# Number of votes for each senator
	most_similar_sen = ''
	similarity_score = -VOTES;

	for sen_b in voting_dict.keys():
		if sen == sen_b:
			continue
		
		score = policy_compare(sen, sen_b, voting_dict)

		if score > similarity_score:
			most_similar_sen = sen_b
			similarity_score = score

	return most_similar_sen


print(most_similar('Kennedy', senators_dict))


# Task 2.12.4: Write a very similar procedure least similar(sen, voting dict) that
# returns the name of the senator whose voting record agrees the least with the senator whose
# name is sen.
def least_similar(sen, voting_dict):
	VOTES = 46						# Number of votes for each senator
	least_similar_sen = ''
	similarity_score = VOTES;

	for sen_b in voting_dict.keys():
		if sen == sen_b:
			continue
		
		score = policy_compare(sen, sen_b, voting_dict)

		if score < similarity_score:
			least_similar_sen = sen_b
			similarity_score = score

	return least_similar_sen


print(least_similar('Kennedy', senators_dict))

# Task 2.12.5: Use these procedures to figure out which senator is most like Rhode Island
# legend Lincoln Chafee. Then use these procedures to see who disagrees most with Pennsylvania’s
# Rick Santorum. Give their names.

# for sen in senators_dict.keys():
# 	print('Senator ' + sen + ':')
# 	print('most similar:' + str(most_similar(sen, senators_dict)))
# 	print('least similar:' + str(least_similar(sen, senators_dict)))
# 	print()

print('Most similar to Sen. Lincoln is ' + str(most_similar('Lincoln', senators_dict)))
print('Least similar to Sen. Santorum is ' + str(least_similar('Santorum', senators_dict)))

# Task 2.12.7: Write a procedure find average similarity(sen, sen set, voting dict)
# that, given the name sen of a senator, compares that senator’s voting record to the voting
# records of all senators whose names are in sen set, computing a dot-product for each, and
# then returns the average dot-product.
# Use your procedure to compute which senator has the greatest average similarity with
# the set of Democrats (you can extract this set from the input file).
def find_average_similarity(sen, sen_set, voting_dict):
	return sum([policy_compare(sen, sen_b, voting_dict) for sen_b in sen_set]) / (len(sen_set))

print(find_average_similarity('Kennedy', {'Lincoln', 'Santorum', 'Bennett', 'Chambliss'}, senators_dict))


# Task 2.12.8: Write a procedure find average record(sen set, voting dict) that,
# given a set of names of senators, finds the average voting record. That is, perform vector
# addition on the lists representing their voting records, and then divide the sum by the number
# of vectors. The result should be a vector.
# Use this procedure to compute the average voting record for the set of Democrats, and
# assign the result to the variable average Democrat record. Next find which senator’s
# voting record is most similar to the average Democrat voting record. Did you get the same
# result as in Task 2.12.7? Can you explain?
def list2vec(L):
    return Vec({i for i in range(len(L))}, {k:v for k, v in enumerate(L)})

def find_average_record(sen_set, voting_dict):
	D = set(range(46))
	u = Vec(D, {})
	for senator in sen_set:
		v = list2vec(voting_dict[senator])
		u = u + v
	u = u / len(sen_set)
	return u

print(find_average_record({'Lincoln', 'Santorum', 'Bennett', 'Chambliss'}, senators_dict))

u = find_average_record({'Lincoln', 'Santorum', 'Bennett', 'Chambliss'}, senators_dict)
print(list2vec(senators_dict['Kennedy']) * u)


# Task 2.12.9: Write a procedure bitter rivals(voting_dict) to find which two senators
# disagree the most.
def bitter_rivals(voting_dict):
	score = 46
	sen_a = ''
	sen_b = ''
	for a in voting_dict.keys():
		for b in voting_dict.keys():
			similarity_score = policy_compare(a, b, voting_dict)
			if(similarity_score < score):
				score = similarity_score
				sen_a = a
				sen_b = b	
	return (sen_a, sen_b, score)

print(bitter_rivals(senators_dict))





