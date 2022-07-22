import random

#to import the functions -> python -> from AtomProb import *
# to simulate n sided die -> to run func type >>>AtomProb.die(n)
def roll_dice():
    return random.randint(1,6)

def roll_NSdice(n):
    return random.randint(1,n)

# to simulate a collection of dice
def roll_dices(n, m):
    return [roll_dice(n) for i in range(m)]

    #for i in range(0,m):
        #print(random.randint(1,n))

#dice rolls
def dice_exp(n):
    freq = {}
    for i in range(n):
        roll = roll_dice()
        if roll in freq:
            freq[roll] += 1
        else:
            freq[roll] = 1
    return freq


#dice rolls with n sides
def dice_sides_exp(n, nSides):
    freq = {}
    for i in range(n):
        roll = roll_NSdice(nSides)
        if roll in freq:
            freq[roll] += 1
        else:
            freq[roll] = 1
    return freq
