import itertools
from sympy.combinatorics import Permutation, Cycle
from sympy.combinatorics.subsets import Subset

A = set([1,2])
B = set([2,3])
C = set([3,4])
D = set(['a', 'b', 'c'])
#a = Subset(['a','b'], ['a','b','c'])

print(A | B) #for 'AUB'
print(A & B) #for 'AnB'
print((A-B) | (B-A))
print(A&A)
print(A- (A-B))
#print(a.cardinality())
#for subset '<='
#for direct subset '<'

print(A | (B & C) == (A | B) & (A | C))
print(A <= (B | C) == A <= B and A <= C)
print((A-B) == (B-A))
print(A-(B | C) == (A-B) | (A-C))
print(A- (B & C) == (A - B) & (A - C))
print(A-(B&C))
print((A-B)&(A-C))
#a = {1}
#b = {1, 2}
#c = {{1},{1, 2}}
#print(*itertools.products(a,b))

l = [1,2,3,4] #<---change list to [whatever] to find powerset

def powerset(cs):
    results = [[]]
    for i in cs:
        new_sub = [subsets+[i] for subsets in results]
        results.extend(new_sub)
    return results

print(powerset(l))
#print(len(powerset(l))) == 2**n(ele) in a set ->for no of ele in powerset

ok = {1,2}
ok1 = {2,3}
ok2 = {3,4}
#if ok <= ok1 and ok1 <= ok2 and ok <= ok2:
    #print('yhh')
#else:
    #print('nah')
