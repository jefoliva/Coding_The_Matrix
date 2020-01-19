def makeInverseIndex(strlist):
    docs = list(strlist)
    dic = {}
    for (i, doc) in enumerate(docs):
        for word in doc.split():
            if word in dic.keys():
                newval = dic[word]
                newval.add(i)
                dic[word] = newval
            else:
                dic[word] = {i}
    return dic

def orSearch(inverseIndex, query):
    matchsets = set()
    for word in query:
        if word in inverseIndex:
            matchsets.update(inverseIndex[word])
    return matchsets


def andSearch(inverseIndex, query):
    matchsets = set()
    for word in query:
        if word in inverseIndex:
            if(len(matchsets) == 0):             # if set is empty
                matchsets.update(inverseIndex[word])
            else:
                matchsets = matchsets.intersection(inverseIndex[word])
                if len(matchsets) == 0:
                    return set()
    return matchsets


inverseIndex = makeInverseIndex(open('Material/stories_small.txt'))
print(orSearch(inverseIndex, ['Communist']))
print(andSearch(inverseIndex, ['the', 'top']))
print(andSearch(inverseIndex, ['off', 'as', 'over']))


# Problem 0.8.4: inv dict(d)
# input: dictionary d representing an invertible function f
# output: dictionary representing the inverse of f, the returned dictionary’s keys are the values of
# d and its values are the keys of d
def inv_dict(d):
    return {v:k for k,v in d.items()}

lang_dict = {'merci':'thank you', 'au revoir':'goodbye'}
inverse_dict = inv_dict(lang_dict)
print(lang_dict['merci'])
print(inverse_dict['thank you'])

# Problem 0.8.5: First write a procedure row(p, n) with the following spec:
#  input: integer p, integer n
#  output: n-element list such that element i is p + i
#  example: given p = 10 and n = 4, return [10, 11, 12, 13]
def row(p, n):
    return [p+i for i in range(n)]

print(row(10, 4))