'''The game is that the computer "thinks" about a number and we have to guess it. On every guess, the computer will tell us if our guess was smaller or bigger than the hidden number. The game ends when we find the number.Also Define no of attemps took to find this hidden number.(Hidden number lies between 0 - 100)'''

import random

def guess(n):
    c=1
    while True:
        k=int(input("Guess a number: "))
        if(k==n):
            print("You have won the game")
            break
        else:
            if(k<n):
                print("Hidden number is greater")
            else:
                print("Hidden number is lesser")
        c+=1
    print("You have taken",c,"chances to find the hidden number")
    

H=random.randint(0,100)
guess(H)
