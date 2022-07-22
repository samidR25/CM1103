import itertools
import math

#-------->if/ order matters/ prize not the same => perm
#-------->if order doesn't matter => comb


#-----> Permutations = n!
#-----> Permutations(for r (e.g 2) in n)
# formula = n!/(n-r)!

A = {1,2,3}
for i in itertools.permutations(A, 2):
    print(i,'perm')

#print(*itertools.permutations(range(0,6), 2))##

#-----> Combinations(for r (e.g 2) in n) - C(n,r)
# formula = n!/r!(n-r)!

for i in itertools.combinations(A, 2):
    print(i,'comb')

#print(*itertools.combinations(range(0,6), 2))##


#-----> Repetitions+ perm = n**r
#-----> Repetitions+ comb C(n+r-1, r)


#indistinguishable objects- e.g, Repeates letters in words i.e; 'scareceness'
# formula = n!/(n!n2!...nk!)
