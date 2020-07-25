'''Develop a Python Program which prints factorial of a given number (Number should be User defined)'''

def factorial(n):                          # calling function to calculate factorial of given number
    if n<0:                                # checking if n is positive or not  
        print("Enter a positive number")   # if negative print to entner positive number
    elif n==0:                             # checking whether n is 0 or not
        return 1                           # if 0 return 1 as the factorial of 0 is 1
    else:                                  # if n is positive
        return factorial(n-1)*n            # return the multiplication of  calling the function(recursion) to 1 less to n and n
    
n=int(input("Enter a number : "))          # taking the input of a number for which we need factorial 
k=factorial(n)                             # taking a variable and calling function and the returned value from the function is assigned to variable
print("Factorial of",n,"is",k)             # printing the factorial of given number 
