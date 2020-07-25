'''The game is that the computer "thinks" about a number and we have to guess it. On every guess, the computer will tell us if our guess was smaller or bigger than the hidden number. The game ends when we find the number.Also Define no of attemps took to find this hidden number.(Hidden number lies between 0 - 100)'''

import random

def guess(n):
    c=1
    a=0
    while c<=5:
        k=int(input("Guess a number: "))
        if(k==n):
            print("Hidden number is",H,",You have won the game in",c,"chances")
            a=1
            break
        elif(c!=5):
            if(k<n):
                print("Hidden number is greater, Guess again")
            else:
                print("Hidden number is lesser, Guess again")
        c+=1
    if(a==0):
        print("Sorry, Your chances are over")
    
H= random.randint(0,100)
guess(H)


