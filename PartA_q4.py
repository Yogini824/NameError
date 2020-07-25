'''Write a Python program to calculate sum and product of digits of a number.(Create Two different funtions one for sum and one product.)'''

def summing(n):                             # defining function to calculate the sum of digits of a number
    s=0                                     # taking a variable to store sum
    k=n                                     # copying the value of n for the use of condition in while
    while k>0:                              # taken while loop to run upto k becomes 0
        s+=k%10                             # adding the last digit of the number to the sum
        k//=10                              # last digit is removed from the number
    print("Sum of digits of",n,"is",s)      # printing the sum of digits of the number

def product(n):                             # defining function to calculate the product of digits of number
    p=1                                     # taking a variable to store product
    k=n                                     # copying the value of n for the use of condition in while
    while k>0:                              # taken while loop to run upto k becomes 0  
        p*=k%10                             # multiplying the last digit of the number to the product 
        k//=10                              # last digit is removed from the number
    print("Product of digits of",n,"is",p)  # printing the product of digits of the number
    
n=int(input("Enter a number : "))           # number is taken as input
summing(n)                                  # calling function to calculate the sum of digits of given number
product(n)                                  # calling function to calculate the product of digits of given number
