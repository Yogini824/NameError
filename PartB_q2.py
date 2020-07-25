'''Develop a Python program to print all Prime numbers in a given Interval (Interval values should be user defined)'''

def prime(a,b):                                                # defining a function to take 2 values lower and upper interval
    print("Prime numbers between",a,"and",b,"are : ",end=" ")  # printing the statement
    for i in range(a,b+1):                                     # taken for loop to run from lower to upper interval
        c=0                                                    # taken a variable for reference to check whether number is divisible or not
        for j in range(2,(i//2)+1):                            # taken for loop to run from 2 to half of a number 
            if i%j==0:                                         # checking the condition whether a number is divisible by 2 to half of it or not
                c=1                                            # if divisible making c to 1 for refenence to know that it is not prime
                break                                          # if c=1 then the number is not prime so we can break the loop as there is no need to run the loop further
        if(c==0):                                              # if c=0 the numnber is prime
            print(i,end=" ")                                   # if the condition is true then print the prime number

a=int(input("Enter the lower interval value : "))              # taking the input of lower interval
b=int(input("Enter the upper interval value : "))              # taking the input of upper interval  
prime(a,b)                                                     # calling the function to check and print primes between a and b 
