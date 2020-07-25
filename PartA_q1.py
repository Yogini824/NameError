'''Write a program that prints the next 20 leap year and sum of digits of leap year must be greater than 16'''

def sum_of_digits(y):    # defining function to calculate the sum of digits of an year
    s=0                  # taking sum as 0
    n=y                  # taking variable n to take the value of y
    while n>0:           # Running while loop upto n becomes 0
        s+=n%10          # adding the remainders to get the sum of digits
        n//=10           # removing the last digit after adding by using division
    return s             # returning the sum to check it is greater than 16 or not


def leap_year(y):                            # defining a function to check the year is a leap or not
    if y%4==0 or (y%400==0 and y%100!=0):    # if year divisible by 4 or divisible by 400 and should not be divisible by 100 then it is a leap year
        return sum_of_digits(y)              # if y is leap year then calling the function to calculate the sum of digits
    else:                               
        return 0                             # if not then returning value 0

def output(n):           # defining a function to print given number of leap years
    k=0                  # taken a variable to count number of leap years
    p=2020               # taken a variale p with value 2020 as we have to print the next leap years of 2020
    while k<n:           # taken a while loop to run upto n number of leap years
        p+=4             # As the leap year comes in the gap of 4 years, adding the current year to 4
        c=leap_year(p)   # calling the leap_year function to get the sum of digts which is the function furthur called in leap_year
        if c>16:         # condition checking if the sum of digits greater than 16 or not
            print("Year =",p,"   Sum of digits =",c)     # if condition is true we will print the year
            k+=1         # updating k value adding 1 to count number of leap years
    
n=int(input("Enter number of leap years needed that sum of digits are greater than 16 : "))  # taking input for numbers of leap years we needed according to question
output(n)                # calling the function to get the required output

    
    
    
