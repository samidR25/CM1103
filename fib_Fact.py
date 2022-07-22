def F(n):
    if n == 1 or n ==2:
        return 1 #base case
    else:
        return F(n-1)+F(n-2) # recursive step

print(F(25))

def Ff(n):
    print(f"Ff({n}) called")
    if n == 1 or n ==2:
        return 1 #base case
    else:
        r = Ff(n-1)+Ff(n-2) # recursive step
        print(f"Ff({n}) returns {r}")
        return r


        def Fact(n):
            if n == 0:
                return 1
            else:
                return n*Fact(n-1)

        print(Fact(3))

#print(Ff(3))
