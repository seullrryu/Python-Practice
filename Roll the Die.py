"""
RyuSeulmin_assign8_part1.py

Written by: Seulmin Ryu

Date: 11/26/2017

Section 003

"""

import random

sides = int(input("How many sides to your die (3-20)?"))
while True:
    if sides <= 3 or sides >= 20:
        print("Sides must be between 3 and 20. Try again.")
        sides = int(input("How many sides to your die (3-20)?"))

    elif 3 < sides < 20:
        break


rolls = int(input("How many rolls do you want?"))
while True:
    if rolls <= 0:
        print("Can't roll", rolls, "times.", "Try again.")
        rolls = int(input("How many rolls do you want?"))

    elif rolls > 0:
        print()
        print("Here we go!")
        break

print()
print("Frequency Analysis:")

rolllist = []
count = 0
    
while count < rolls:
    num = random.randint(1,sides)
    rolllist.append(num)
    count = count + 1


countlist = []
for i in range(1, sides+1):
    x = rolllist.count(i)
    countlist.append(x)


if max(countlist) > 50:
    increment = ((max(countlist) // 50) + 1)
    print("Each * represents", increment, "rolls")
    
else:
    increment = ((max(countlist) // 50) + 1)
    print("Each * represents", increment, "roll")
    

for j in range(1, sides+1):
    if max(countlist) > 50:
        
        numstar = ((countlist[j-1])//increment)
        
        numspace = len(str(countlist[j-1]))
        space = str(numspace)+"d"
        
        print("Side", format(j,'2d'), ":", format(countlist[j-1], ">" + str(space)), "times:", "*"*numstar)
    
    else:
        print("Side", format(j,'2d'), ":", format(countlist[j-1],'2d'), "times:", "*"*countlist[j-1])



print("Total Rolls:", rolls)

    

    




