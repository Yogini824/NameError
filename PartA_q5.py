'''Write a Python program to calculate area and perimeter of square,rectangle,Rhombus,parallelogram.(Create Two different funtions one for Area and one for Perimeter.)'''

import math

def area():                                                            # defining the function to calculate area
    s=float(input("Enter the side of sqaure : "))                      # take side of square as input
    print("Area of square with side",s,"is",s*s)                       # printing the area of square  
    d1=float(input("Enter the first diagonal of rhombus : "))          # take first diagonal of rhombus as input
    d2=float(input("Enter the second diagonal of rhombus : "))         # take second diagonal of rhombus as input
    print("Area of rhombus with diagonal",d1,"and diagonal",d2,"is",d1*d2/2) # printing the area of rhombus
    l=float(input("Enter the length of rectangle : "))                 # take length of rectangle as input
    b=float(input("Enter the breadth of reactangle : "))               # take breadth of rectangle as input 
    print("Area of rectangle with length",l,"and breadth",b,"is",l*b)            # printing the area reactangle
    b=float(input("Enter the base of parallelogram : "))             # take the legnth of parallelogram  
    h=float(input("Enter the height of parallelogram : "))            # take the breadth of parallelogram
    print("Area of parallelogram with base",b,"and height",h,"is",b*h)        # printing the area of parallelogram 

def perimeter():                                                       # defining the function to calculate perimeter                                        
    s=float(input("Enter the side of sqaure : "))                      # take side of square as input
    print("Perimeter of square with side",s,"is",4*s)                  # printing the perimeter of square  
    d1=float(input("Enter the first diagonal of rhombus : "))          # take first diagonal of rhombus as input
    d2=float(input("Enter the second diagonal of rhombus : "))         # take second diagonal of rhombus as input
    print("Perimter of rhombus with diagonal",d1,"and diagonal",d2,"is",pow(pow(d1/2,2)+pow(d2/2,2),1/2))# printing the perimeter of rhombus
    l=float(input("Enter the length of rectangle : "))                 # take length of rectangle as input
    b=float(input("Enter the breadth of reactangle : "))               # take breadth of rectangle as input
    print("Perimeter of rectangle with length",l,"and breadth",b,"is",2*(l+b))   # printing the perimeter reactangle 
    d1=float(input("Enter the first diagonal of parallelogram : "))          # take first diagonal of parallelogram as input
    d2=float(input("Enter the second diagonal of parallelogram : "))         # take second diagonal of parallelogram as input
    print("Perimter of parallelogram with diagonal",d1,"and diagonal",d2,"is",pow(pow(d1/2,2)+pow(d2/2,2),1/2))  # printing the parallelogram of rhombus

area()                                                                 # calling function to calculate area
perimeter()                                                            # calling function to calculate perimeter
