'''Develop a python program which print sum of all the Integers in a list ( Note  : All the elements must be user defined and list must contain strings also ) '''

def list_input(n):                                   # defining function to take n number of inputs and get sum of integers
    s=0                                              # taken a variable to get sum of integers
    l=[]                                             # take an empty list to add the elements
    print("Enter the elements to the list")          # printing to enter the elements
    for i in range(n):                               # taken a for loop to run for n times to take n inputs  
        l.append(input())                            # adding the input taken to list
        if(l[-1].isdigit()!=0):                      # checking if the element added is a digit or not
            s+=int(l[-1])                            # if it is digit then add it to sum
    print("The sum of all integers in list is",s)    # printing the sum after adding all the integers
        
n=int(input("Enter number of elements in list : "))  # taking input integer for numbers of elements in list
list_input(n)                                        # caling function to take n elements and get the sum of integers
