'''Develop a Python Program which prints cube sum of first n natural numbers (N is user defined)'''

def cube_sum(n):                                    # defining  a function to get cube sum of n natural numbers
    s=0                                             # taken a variable to get sum and intialized with 0
    for i in range(1,n+1):                          # take for loop to run from 1 to n
        s+=(i**3)                                   # taking the cubes of numbers and adding
    print("Cube_sum of",n,"natural numbers is",s)   # printing the cube sum


n=int(input("Enter a number : "))                   # taking input for n natural numbers
cube_sum(n)                                         # calling the function to get the cube sum
