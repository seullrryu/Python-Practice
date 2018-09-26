"""
RyuSeulmin_assign7_part3.py

Written by: Seulmin Ryu

Date: 11/15/2017

Section 003

"""
import random

# generate_code
# Input: length (int)
# Processing: generate a secret code.  The code should have the number of digits specified by length, 
#             using the digits 1 - 9, and without any repeats.
# Return: the secret code (str)
def generate_code(length):
    code = ""
    for i in range(length):
        num = str(random.randint(1,9))  
        while num in code:
            num = str(random.randint(1,9))
        code = code + num
    return code
                

# digits_in_code
# Input: guess (str), code (str)
# Processing: count each digit in guess that also appears in the code
# Return: the count (int)
def digits_in_code(guess, code):
    count = 0
    for i in str(guess):
       if i in code:
            count = count + 1
    return count



# digits_in_place
# Input: guess (str), code (str)
# Processing: count each digit that appears in the same place in both guess and code
# Return: the count (int)
def digits_in_place(guess, code):
    correct = 0
    for i in range(length):
        if guess[i] == code[i]:
            correct = correct + 1
    return correct



length = int(input("How long should the secret code be?"))
if length > 8 or length < 2:
    print("Code must be between 2 and 8 digits long.")
    while True:
        length = int(input("How long should the secret code be?"))
        if 2 <= length <= 8:
            break
        

count = 0
code = generate_code(length)
while True:
    guess = input("What is your guess?")
    
    if len(guess) != length:
        print("Guess must be", length, "digits long")
        guess = input("What is your guess?")

    count = count + 1

    if guess != code:
        print(digits_in_code(guess, code), "are in the code and", digits_in_place(guess, code), "are in the correct place")
    else:
        print("You guessed it in", count, "turns!")
        break
