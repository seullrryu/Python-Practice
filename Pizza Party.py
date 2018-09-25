"""
RyuSeulmin_assign5_problem1.py

Written by: Seulmin Ryu

Date: 10/29/2017

Section 003

"""

while True:
    budget = float(input("Enter budget for your party:"))
    slicecost = float(input("Cost per slice of pizza:"))
    piecost = float(input("Cost per whole pizza pie (8 Slices):"))
    ppl = int(input("How many people will be attending your party?"))

    if budget < 0 or slicecost < 0 or piecost < 0 or ppl < 0:
        print("Not a vaild entry, try again!")
        break    
    
    total = 0
    count = 0
    for i in range(1, ppl+1):
        Q = "Enter number of slices for person " + str(i) + ":"
        numslices = int(input(Q))

        if numslices < 0:
            print("Not a vaild entry, try again!")
            numslices = int(input(Q))
                               
        total = total + numslices
        count = count + 1

        pie = total // 8
        otherslices = total % 8

    cost = ((otherslices*slicecost) + (pie * piecost))
    fcost = format(cost, ".2f")

    leftover = budget - cost
    negLeftover = (-1 * leftover)
    
    fleftover = format(leftover, ".2f")
    fnegLeftover = format(negLeftover, '.2f')

    print("You should purchase", pie, "pies", "and", otherslices, "slices")
    print("Your total cost will be:", fcost)

    if leftover > 0:
        print("You will still have", fleftover, "left after your order")
    elif leftover == 0:
        print("You will have no money left after your order.")
    elif leftover < 0:
        print("This would put you over budget by", fnegLeftover)

    if count == ppl:
        break 
