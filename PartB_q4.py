'''Develop a Python Program to check if a given string is palindrome or not ? (Example for an Palindrome is abcba looks same from both ends)'''

def palindrome(s):                           # defining function to check whether given string is palindrome or not
    a=0                                      # taken the starting index
    b=len(s)-1                               # taken the ending index
    c=0                                      # taken a variable for reference to check given string is palindrome or not
    while True:                              # taken a while loop to run multiplt times
        if(s[a]!=s[b]):                      # checking the starting index values and ending index values are same or not
            print(s,"is not a palindrome")   # if not then printing the given string is not palindrome
            c=1                              # updating the variable for reference 
            break                            # breaking the loop as string is not palindrome and there is no need to check furthur   
        else:                                # if the values are same
            if a==b or b-a==1:               # and a, b are same are b is 1 greater than a
                break                        # we should break the loop 
            a+=1                             # if not then increment the index value a   
            b-=1                             # and decrement b
    if(c==0):                                # if c=0 then string is palindrome
        print(s,"is a palindrome")           # printing given string is palindrome
        
        
s=input("Enter a string : ")                 # taking string as input 
palindrome(s)                                # calling the function to check given string is palindrome is not
