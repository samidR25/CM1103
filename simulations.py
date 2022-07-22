import random

# Roll a six-sided die
def rollDice():
    return random.randint(1, 6)

# Roll an n-sided dice
def rollNSidedDice(n):
    return random.randint(1, n)

# Roll m n-sided dice
def rollMultipleDice(n, m):
   return [rollNSidedDice(n) for i in range(m)]


# Test n rolls of a dice with 6 sides
def diceExperiment(n):
    freq = {}
    for i in range(n):
        roll = rollDice()
        if roll in freq:
            freq[roll] += 1
        else:
            freq[roll] = 1
    return freq


# Test n rolls of a die with nSides sides
def diceExperimentForNSides(n, nSides):
    freq = {}
    for i in range(n):
        roll = rollNSidedDice(nSides)
        if roll in freq:
            freq[roll] += 1
        else:
            freq[roll] = 1
    return freq


#############################################################


# Rolling a die with a coin
def rollDiceByCoin():
    outcomes = []
    if random.randint(0, 1) == 0:
        outcomes = [1, 2, 3]
    else:
        outcomes = [4, 5, 6]

    while True:
        if random.randint(0, 1) == 0:
            if random.randint(0, 1) == 1:
                return outcomes[0]
        else:
            if random.randint(0, 1) == 0:
                return outcomes[1]
            else:
                return outcomes[2]

# A different way to roll a die with a coin
def rollDiceByCoin2():
    roll = random.randint(1, 8)
    while roll > 6:
        roll = random.randint(1, 8)
    return roll


# Rolling a die with a coin, count the number of coin flips used
def rollDiceByCoincounttoss():
    tosses = 0
    outcomes = []
    tosses += 1
    if random.randint(0, 1) == 0:
        outcomes = [1, 2, 3]
    else:
        outcomes = [4, 5, 6]

    while True:
        tosses += 2
        if random.randint(0, 1) == 0:
            if random.randint(0, 1) == 1:
                return tosses, outcomes[0]
        else:
            if random.randint(0, 1) == 0:
                return tosses, outcomes[1]
            else:
                return tosses, outcomes[2]


# A different way to roll a die with a coin, count the number of coin flips used
def rollDiceByCoin2counttoss():
    tosses = 0
    roll = random.randint(1, 8)
    tosses +=3
    while roll > 6:
        roll = random.randint(1, 8)
        tosses += 3
    return tosses, roll


# Experiment but count the number of coin flips used
def diceExperimentCountFlips(n, rollFunction):
    total = 0
    freq = {}
    for i in range(n):
        t, roll = rollFunction()
        total += t
        if roll in freq:
            freq[roll] += 1
        else:
            freq[roll] = 1
    return total / float(n), freq


#########################################################

def fy_shuffle(a):
    for i in range(len(a), 0, -1):
        n = random.randrange(0, i)
        a[i - 1], a[n] = a[n], a[i - 1]
    return a


def shuffle(a):
    for i in range(0, len(a)):
        n = random.randint(0, len(a) - 1)
        a[i], a[n] = a[n], a[i]
    return a

# Test the fisher yates shuffle
def experiment(n):
    freq = {}
    for i in range(n):
        roll = tuple(fy_shuffle([1, 2, 3]))
        if roll in freq:
            freq[roll] += 1
        else:
            freq[roll] = 1
    return freq
