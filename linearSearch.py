import random

def linearSearch(list, key):
    for i, x in enumerate(list):
        if x == key:
            return i
    return -1

#a = random.sample(list(range(100)),k = 6)
#print(a)
list = [12,35,56,87]
print(linearSearch(list,87))

# average case = n+1/2
# unsuccessful + worst case = n comparisons (total n, the last n value)
