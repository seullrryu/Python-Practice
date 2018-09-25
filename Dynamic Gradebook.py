"""
RyuSeulmin_assign5_problem2.py

Written by: Seulmin Ryu

Date: 10/29/2017

Section 003

"""

students = int(input("How many students are in your class?"))
while True:
    if students < 0:
        print("Invaild number of students, try again.")
        students = int(input("How many students are in your class?"))
    else:
        break 

tests = int(input("How many tests in this class?"))
while True: 
    if tests < 0:
        print("Invaild number of students, try again.")
        tests = int(input("How many tests in this class?"))
    else:
        break 


count = 0
total = 0
for x in range(1, students+1):
    print("Student #", x)
    subtotal = 0
    
    for i in range(1, tests+1):
        count = count + 1
        
        Q = "Enter score for test #" + str(i) + ":"
        score = float(input(Q))
        
        if score < 0:
            print("Invaild score, try again.")
            score = float(input(Q))

        total = total + score 
        subtotal = subtotal + score

        global avg
        avg = (subtotal / tests)

        global favg
        favg = format(avg, '.2f')


    print("Average score for student #", x, favg)
    

realavg = total / count
frealavg = format(realavg, '.2f')
print("Average score for all students is:", frealavg)
