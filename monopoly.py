import numpy
import matplotlib.pyplot as plt
from random import randint  

maxdig = 3

numtrials = 100
gamelen = 100

squares = numpy.arange(40)


# Properties 

brown = [1,3] # the positions of the brown properties
# this is the second comment line 
lightblue = [6,8,9] 
pink = [11,13,14]
orange = [16,18,19] 
red = [21,23,24]
yellow = [26,27,29] 
green = [31,32,34] 
darkblue = [37,39]

properties = brown + lightblue + pink + orange + red + yellow + green + darkblue

fb = [0]*numtrials
flb = [0]*numtrials
fp = [0]*numtrials
fo = [0]*numtrials
fr = [0]*numtrials
fy = [0]*numtrials
fg = [0]*numtrials
fdb = [0]*numtrials

# Railroads 

reading = 5
pennsylvania = 15
bo = 25
short = 35

railroads = [reading, pennsylvania, bo, short] 


# Utilities

electric = 12
water = 28 

utilities = [electric, water] 


# Special 

chance = [7,22,36]
commchest = [2,17,33]

# Penalties 

luxurytax = 28
incometax = 4 

penalties = [luxurytax, incometax] 

# Jail 

gotojail = 30
jail = 10

# Rolling 
chancecards = numpy.arange(1,18).tolist()
commchestcards = numpy.arange(1,18).tolist()

def chancecard(pos):
    global chancecards
    card = randint(1,18)
    while(card not in chancecards):
        card = randint(1,18)
    chancecards.remove(card)
    if(len(chancecards)==0):
        #print("No more chance cards :(") 
        chancecards = numpy.arange(1,18).tolist()
    if(card == 1):
        return 0
    elif(card == 2): 
        return 24
    elif(card == 3):
        mindist = 21
        nearestutil = -1
        for i in range(len(utilities)):
            dist = 0 
            if(utilities[i]<pos):
                dist = (40-pos)+utilities[i]
            else:
                dist = utilities[i]-pos
            if(dist < mindist):
                mindist = dist
                nearestutil = utilities[i]
        return nearestutil
    elif(card == 4):
        mindist = 21 
        nearestrailroad = -1 
        for i in range(len(railroads)):
            dist = 0 
            if(railroads[i]<pos):
                dist = (40-pos)+railroads[i]
            else:
                dist = railroads[i]-pos
            if(dist < mindist): 
                mindist = dist 
                nearestrailroad = railroads[i]
        return nearestrailroad 
    elif(card == 5):
        return 11 
    elif(card == 6):
        return pos-3 
    elif(card == 7):
        return jail 
    elif(card == 8):
        return 5
    elif(card == 9): 
        return 39 
    else:
        return pos  
    
def commchestcard(pos): 
    global commchestcards
    card = randint(1,18)
    while(card not in commchestcards):
        card = randint(1,18)
    commchestcards.remove(card)
    if(len(commchestcards) == 0):
        #print("No more commchest cards :(")
        commchestcards = numpy.arange(1,18).tolist()
    if(card == 1):
        return 0 
    elif(card == 2):
        return jail 
    else:
        return pos 

for trial in range(numtrials):
    freq = [0]*40
    pos = 0 
    for roll in range(gamelen): 
        pos += randint(1,6)
        pos += randint(1,6)
        pos = pos%40
        if(pos == gotojail):
            freq[pos] += 1
            pos = jail 
        elif(pos in chance):
            pos = chancecard(pos)
        elif(pos in commchest):
            pos = commchestcard(pos)
        freq[pos] += 1
    
    for i in range(len(brown)):
        fb[trial] += freq[brown[i]]
    for i in range(len(lightblue)):
        flb[trial] += freq[lightblue[i]]
    for i in range(len(pink)):
        fp[trial] += freq[pink[i]]
    for i in range(len(orange)):
        fo[trial] += freq[orange[i]]
    for i in range(len(red)):
        fr[trial] += freq[red[i]]
    for i in range(len(yellow)): 
        fy[trial] += freq[yellow[i]]
    for i in range(len(green)):
        fg[trial] += freq[green[i]]
    for i in range(len(darkblue)):
        fdb[trial] += freq[darkblue[i]]



# Printing 

print("Brown: " + str(numpy.mean(fb)) + " +/- " + str(numpy.std(fb)))
print("Light blue: " + str(numpy.mean(flb)) + " +/- " + str(numpy.std(flb)))
print("Pink: " + str(numpy.mean(fp)) + " +/- " + str(numpy.std(fp)))
print("Orange: " + str(numpy.mean(fo)) + " +/- " + str(numpy.std(fo)))
print("Red: " + str(numpy.mean(fr)) + " +/- " + str(numpy.std(fr)))
print("Yellow: " + str(numpy.mean(fy)) + " +/- " + str(numpy.std(fy)))
print("Green: " + str(numpy.mean(fg) ) + " +/- " + str(numpy.std(fg)))
print("Dark blue: " + str(numpy.mean(fdb)) + " +/- " + str(numpy.std(fdb)))


firstlast = " -------------------------------------------"
second = "|---|-----------------------------------|---|"
other = "|---|                                   |---|"
space = "|                                   |"


def ws(val):
    s = str(val)
    for i in range(maxdig-len(str(val))):
        s+=" "
    return s 

print(firstlast)
r1 = "|"
r1 += ws(freq[20])
r1 += "|"
for i in range(1,10):
    r1 += ws(freq[i+20])
    r1 += "|"
r1 += ws(freq[30])
r1 += "|"
print(r1)
print(second)
print("|"+ws(freq[19])+space+ws(freq[31])+"|")
print(other)
print("|"+ws(freq[18])+space+ws(freq[32])+"|")
print(other)
print("|"+ws(freq[17])+space+ws(freq[33])+"|")
print(other)
print("|"+ws(freq[16])+space+ws(freq[34])+"|")
print(other)
print("|"+ws(freq[15])+space+ws(freq[35])+"|")
print(other)
print("|"+ws(freq[14])+space+ws(freq[36])+"|")
print(other)
print("|"+ws(freq[13])+space+ws(freq[37])+"|")
print(other)
print("|"+ws(freq[12])+space+ws(freq[38])+"|")
print(other)
print("|"+ws(freq[11])+space+ws(freq[39])+"|")

print(second)
r10 = "|"
r10 += ws(freq[10])
r10 += "|"
for i in range(9,0,-1):
    r10 += ws(freq[i])
    r10 += "|"
r10 += "GO |"
print(r10)
print(firstlast)


