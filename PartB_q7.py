'''Develop a python program which prints count of all the Characters and strings in a list ( Note  : All the elements must be user defined and list must contain Integers also )'''

def list_input(n):                                   # defining function to take n number of inputs and get sum of characters
    s=0                                              # taken a variable to count number of strings
    c=0                                              # taken avariable to count number of characters
    l=[]                                             # take an empty list to add the elements
    print("Enter the elements to the list")          # printing to enter the elements
    for i in range(n):                               # taken a for loop to run for n times to take n inputs  
        l.append(input())                            # adding the input taken to list
        if(l[-1].isdigit()==0):                      # checking if the element added is a digit or not
            s+=1                                     # if not then count the string
            for j in range(len(l[-1])):              # taken a for loop to run upto length of string times  
                if(l[-1][j].isdigit()==0):           # checking is the character is integer or not
                    c+=1                             # if not then count the character
    print("The numbers of strings are",s)            # printing the number of strings
    print("The number of characters are",c)          # printing the number of characters 
        
n=int(input("Enter number of elements in list : "))  # taking input integer for numbers of elements in list
list_input(n)                                        # caling function to take n elements and get the sum of characters
