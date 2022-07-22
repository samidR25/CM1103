import random

# needs to be sorted
def binarySearch(list, key, i= 0, j= None):
    if j == None:
        j = len(list)-1
    if i>=j:
        if list[i] == key:
            return i
        else:
            return -1
    else:
        mid = (i+j)//2
        if list[mid] == key:
            return mid
        elif key < list[mid]:
            return binarySearch(list, key, i, mid-1)
        else:
            return binarySearch(list, key, mid+1, j)

list = sorted(random.sample(range(100), 40))
print(list)

print(binarySearch(list,35))

# The worst case number of comparisons  is == k
# The worst case number of comparsions for a list of len(n) is log_2(n)+1
#-> approx = log(n) or log_10(n)
