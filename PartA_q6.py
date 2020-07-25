'''Write a function that takes a list of strings an prints them, one per line, in a rectangular frame. For example the list ["Hello", "World", "in", "a", "frame"] gets printed as:
*********
* Hello *
* World *
* in    *
* a     *
* frame *
********* '''

def pattern(l,m):                                            # defining function to print the pattern                  
    n=len(l)+2                                               # taken a variable and added 2 for top and bottom boarders
    for i in range(n):                                       # taken a for loop to run for number of rows
        for j in range(m):                                   # taken a for loop to run for numbers of cloumns
            if(i==0 or i==n-1 or j==0 or j==m-1):            # condition to print *s for boarders
                print("*",end="")                            # printing the *s for boarders if the above condition is true
            elif(j==1 or j==m-2):                            # condition to print space beside the left and right boarders
                print(" ",end="")                            # if true then print the space 
            else:                                            # if not above conditons
                s=len(l[i-1])                                # taken length of every string in list
                if(j-2<s):                                   # condition to check the loop value is less than string length
                    print(l[i-1][j-2],end="")                # if true print the character of string 
                else:                                        # if false
                    print(" ",end="")                        # print space as there is no character remained in the string
        print()                                              # print for next line as we used end="" will not let to next line

def input_list(n):                                           # defining function to take inputs to the list
    l=[]                                                     # taking an empty list to add strings
    print("Enter the strings to the list")                   # printing to enter string inputs
    m=0                                                      # taken a variable to store the largest length of the strings in list
    for i in range(n):                                       # taken for loop to take given number of strings
        l.append(input())                                    # appending the string to list
        if len(l[-1])>m:                                     # condition to take largest length string
            m=len(l[-1])                                     # storing the largest length 
    m+=4                                                     # adding 4 to largest length as we need for 2 spaces and 2 boarders
    return pattern(l,m)                                      # calling function to print the patter after getting the inputs
                
n=int(input("Enter the number of string in the list : "))    # input for number of strings in list
input_list(n)                                                # calling the function to take strings as inputs to list

