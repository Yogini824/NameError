'''Develop a python program which print sum of all the Characters in a list ( Note  : All the elements must be user defined and list must contain Integers also )  '''

def list_input(n):                                   # defining function to take n number of inputs and get sum of characters
    s=""                                             # taken an empty string to get sum of characters
    l=[]                                             # take an empty list to add the elements
    print("Enter the elements to the list")          # printing to enter the elements
    for i in range(n):                               # taken a for loop to run for n times to take n inputs  
        l.append(input())                            # adding the input taken to list
        if(l[-1].isdigit()==0):                      # checking if the element added is a digit or not
            s+=l[-1]                                 # if it is not digit then add it to sum
    print("The sum of all characters in list is",s)  # printing the sum after adding all the characters
        
n=int(input("Enter number of elements in list : "))  # taking input integer for numbers of elements in list
list_input(n)                                        # caling function to take n elements and get the sum of characters
