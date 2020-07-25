'''Design a user interactive Calculator .( sum , subtraction , multiplication , division , Distance , speed , Intrest)'''

def calculator(n):                                        # defining a function for calculation required
    if(n==1):                                             # checking for given number is 1 or not
        a=int(input("Enter 1st number : "))               # if true then take first number as input  
        b=int(input("Enter 2nd number : "))               # take second number as input
        print("Sum of",a,"and",b,"is",a+b)                # print the sum of 2 numbers
    elif(n==2):                                           # checking for given number is 2 or not 
        a=int(input("Enter 1st number : "))               # if true then take first number as input
        b=int(input("Enter 2nd number : "))               # take second number as input
        print("Subtraction of",a,"and",b,"is",a-b)        # print the subtraction of 2 numbers
    elif(n==3):                                           # checking for given number is 3 or not
        a=int(input("Enter 1st number : "))               # if true then take first number as input
        b=int(input("Enter 2nd number : "))               # take second number as input
        print("Multiplication of",a,"and",b,"is",a*b)     # print the multiplication of 2 numbers
    elif(n==4):                                           # checking for given number is 4 or not
        a=int(input("Enter 1st number : "))               # if true then take first number as input
        b=int(input("Enter 2nd number : "))               # take second number as input
        print("Division of",a,"and",b,"is",a/b)           # print the division of 2 numbers
    elif(n==5):                                           # checking for given number is 5 or not
        s=float(input("Enter the speed : "))              # if true then take speed as input
        t=float(input("Enter the time : "))               # if true then take time as input 
        print("Distance of",s,"and",t,"is",s*t)           # print the distance calculated using speed*time
    elif(n==6):                                           # checking for given number is 6 or not
        d=float(input("Enter the distance : "))           # if true then take distance as input 
        t=float(input("Enter number of hours : "))        # take time as input 
        print("Speed of",d,"and",t,"is",d/t)              # print the speed calculated using distance/time
    elif(n==7):                                           # checking for given number is 7 or not
        P=float(input("Enter principle : "))              # if true then take principle as input
        T=float(input("Enter number of years : "))        # take number of years as input 
        R=float(input("Enter rate of interest : "))       # take rate of interest as input
        print("Interest for",T,"years is",P*T*R*0.01)     # print the interest using P*T*R/100
    else:                                                 # checking if not above numbers
        print("Enter a valid number")                     # printing to enter a valid number
    
print("Enter\n1 for Sum\n2 for subtraction\n3 for multiplication\n4 for division\n5 for distance\n6 for speed\n7 for Interest")  # printing and metiong the numbers for calculations
n=int(input("Enter the number : "))   # number taken as input
calculator(n)                         # calling the function for calculation required
      
