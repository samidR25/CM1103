def sqrsum(n):
    i = 1
    total = 0
    while i <= n:
        total = total + i**2
        i = i + 1
        print(i,'ia')
        print(total,'ta')
    return total

#print(sqrsum(4))

def sqrSum1(n):
    if n ==1:
        return 1
    else:
        return n**2 + sqrSum1(n-1)

print(sqrSum1(3))


def sqrsumL(n):
    return [i**2 for i in range(n+1)]

print(sqrsumL(3))

def sumpower(n):
    i = 0
    total = 0
    while i < n:
        print(i, 'ibe')
        print(total, 'tbe')
        total = total + 2**i
        i = i + 1
        print(i, 'iaf')
        print(total, 'taf')
    return total

print(sumpower(3))



def sumpower1(n):
    if n ==1:
        return 1
    else:
        return
