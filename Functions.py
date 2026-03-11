#Example 1: Basic Positional Arguments
"""
def add(a,b):
    print("a=", a) #10
    print("b=", b) #20
    return a + b
result=add(10,20)
print("Sum=", result) #30


#Example 2: Student Information

def student_info(name, age, grade):
    print("Name:", name) #Rushabh
    print("Age:", age)   #18
    print("Grade:", grade) #A
student_info("Rushabh", 18, "A")


#Example 3: Error with wrong number of arguments

#simple interest

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100
# Correct usage
interest = simple_interest(1000, 5, 2)
print("Simple Interest:", interest) #100.0


#Example 4: Area of circle
import math
def area_of_circle(radius):
    return math.pi * radius ** 2
circle_area = area_of_circle(5)
print("Area of Circle:", circle_area) #78.53981633974483
area_of_circle(1.5)
print("Area of Circle:", area_of_circle(1.5)) #7.0685834705770345
area_of_circle(4)
print("Area of Circle:", area_of_circle(4)) #50.26548245743669


#Example 5: Check number positive, negative or zero & odd or even
def check_number(num):
    if num > 0:
        print(num, "is positive")
    elif num < 0:
        print(num, "is negative")
    else:
        print(num, "is zero")
check_number(100) #100 is positive
check_number(-5) #-5 is negative
check_number(0) #0 is zero

def odd_even(num):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")
odd_even(100) #100 is even
odd_even(-5) #-5 is odd


#Example 6: Arithmetic operations Addition, subtraction, multiplication, division
def add(a, b):
    return a + b
result = add(10, 5)
print("Addition:", result) #15

def subtract(a, b):
    return a - b
result = subtract(10, 5)
print("Subtraction:", result) #5

def multiply(a, b):
    return a * b
result = multiply(10, 5)
print("Multiplication:", result) #50

def divide(a, b):
    return a / b
result = divide(10, 5)
print("Division:", result) #2.0
"""