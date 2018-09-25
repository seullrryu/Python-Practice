"""
RyuSeulmin_assign8_part2.py

Written by: Seulmin Ryu

Date: 11/26/2017

Section 003

"""
import random 
cards  = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', 
          '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 
          'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', '10 of Diamonds', 
          '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', 
          '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 
          'Ace of Diamonds', 'King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds', 
          '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', 
          '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', 
          'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', '10 of Spades', 
          '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', 
          '4 of Spades', '3 of Spades', '2 of Spades', 'Ace of Spades', 
          'King of Spades', 'Queen of Spades', 'Jack of Spades']

values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 
          10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 
          4, 3, 2, 1, 10, 10, 10]


playerlist = []
newvalues = []
ctotal = 0
total = 0

#Starting with dealing two cards at random to the player
for i in range(2):
    pick = random.randint(0,len(cards)-1)
    hand = cards[pick]
    
    playerlist.append(hand)
    newvalues.append(values[pick])
    
    del cards[pick]
    del values[pick]

    
#players
while True:
    #finding total
    total = sum(newvalues)

    print("Player hand:", playerlist, "is worth", total)
    choice = input("(h)it or (s)tand?")
    
    #input validation
    while True:
        if choice == 'h' or choice == 's':
            break
        else:
            print("Try Again!")
            choice = input("(h)it or (s)tand?")
            
    if choice == "h":
        pick = random.randint(0,len(cards)-1)
        hand = cards[pick]
        print("You drew", hand)
    
        playerlist.append(hand)
        newvalues.append(values[pick])

        total = sum(newvalues)
        
        del cards[pick]
        del values[pick]

    if total > 21:
        print("Player hand:", playerlist, "is worth", total)
        print("Bust!")
        print("Computer wins!")
        break

    elif total == 21:
        print("Player got 21! Blackjack!")
        print("Player wins!")
        break

# for computers 
    if choice == "s" and total < 21:
        
        complist = []
        compvalues = []

        #Starting with dealing two cards at random to the computer
        for c in range(2):
            cpick = random.randint(0,len(cards)-1)
            chand = cards[cpick]
            
            complist.append(chand)
            compvalues.append(values[cpick])
            
            del cards[cpick]
            del values[cpick]

            
        #finding computer's total
        while True:
            ctotal = sum(compvalues)

            print("Computer hand:", complist, "is worth", ctotal)
            
            cpick = random.randint(0,len(cards)-1)
            chand = cards[cpick]
            print("Computer drew", chand)
            
            complist.append(chand)
            compvalues.append(values[cpick])

            ctotal = sum(compvalues)
            
            del cards[cpick]
            del values[cpick]

            if ctotal > 21:
                print("Computer hand:", complist, "is worth", ctotal)
                print("Bust!")
                print("Player wins!")
                break

            elif ctotal < 21 and ctotal > total:
                print("Computer wins!")
                break 

            elif ctotal == 21:
                print("Computer got 21! Blackjack!")
                print("Computer wins!")
                break
            
        break
