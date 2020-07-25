'''Develop a Python Program which prints factorial of a given number (Number should be User defined)'''

def factorial(n):                         # defining function to calculate factorial of a number
    if n<0:                               # condition to check the number is negative or not
        print("Enter a positive number")  # print to enter positive number if the condition is true
    elif n==0:                            # condition to check the number is 0 or not
        print("Factorial of 0 is 1")      # print the factorial of 0 is the condition is true   
    else:                                 # if the number is positive
        fact=1                            # take a variable to store the factorial of a given number
        for i in range(1,n+1):            # taken for loop to run from 1 to given number
            fact*=i                       # multiplying the numbers and storing it in variable
        print("Factorial of",n,"is",fact) # print the factorial value of given number
            
    
n=int(input("Enter a number : "))         # to take number as input  
factorial(n)                              # calling the function to get factorial value

