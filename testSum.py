

def sum1(n):
    i = 1
    total = 0
    while i <= n:
        total = total + i
        print(total,'total')
        i = i + 1
        print(i,'i')
    return total

#print(sum(5))

def sum2(n):
    i = 1
    total = 0
    for x in range(0,n):
        while i <= n:
            total = total + i
            print(total,'total')
            i = i + 1
            print(i,'i')
        return total

#print(sum2(5))

def sum3(n):
    if n==1:
        print(n,'f')
        return 1
    else:
        print(n,'s')
        return n + sum3(n-1)

#print(sum3(5))

def power(n):
    exp = 1
    for i in range(0,n):
        print(exp, 'b')
        exp = exp * 2
        print(exp, 'a')
    return exp

#print(power(4))

def power1(n):
    if n == 1:
        return 1#base case
    else:
        return 2**(n)#recursive step


#print(power1(5))

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(84,126))
