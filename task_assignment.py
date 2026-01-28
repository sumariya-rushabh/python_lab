Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q.1 Find simple interest
p=float(input("enter principal:"))
enter principal:12
r=float(input("enter rate of interest:"))
enter rate of interest:9999
t=float(input("enter time (years):"))
enter time (years):102
si=(p*r*t)/100
print(f"Simple interest:{si}")
Simple interest:122387.76



#Q.2 Find maximum of 2 numbers
num1= float(input("Enter first number:"))
Enter first number:9
num2= float(input("Enter second number:"))
Enter second number:7
print(f"The maximum is: max{num1,num2}")
The maximum is: max(9.0, 7.0)



#Q.3 print 1 to 5
print(1,2,3,4,5)
1 2 3 4 5



#Q.4 Find length of string
text = input ("enter a string")
enter a string9
print(f"The length of the string is : {len(text}")
SyntaxError: f-string: closing parenthesis '}' does not match opening parenthesis '('
print(f"The length of the string is : {len(text)}")
The length of the string is : 1



#Q.5 print a welcome message
name = input("Enter your name: ")
Enter your name: RUSHABH
print(f"Welcome to python programming language ,{name}!")
Welcome to python programming language ,RUSHABH!



#Q.6 Print first character of a string
text= input("Enter a string:")
Enter a string:RUSHABH
s="RUSHABH"
print(s[:1])
R



#Q.7 Print last character of string
s="python programming"
print(s[-1])
g



#Q.8 Check positive or negative
num = int(input("Enter a number:"))
Enter a number:9
if num> 0:
    print("positive")
    elif num < 0:
        
SyntaxError: invalid syntax
print("Positive" if num > 0 else "Negative" if num < 0 else "Zero")
Positive



#Q.9 Add three numbers
a= float (input("num1: "))
num1: 99
b= float (input("num2: "))
num2: 33
KeyboardInterrupt
c= float (input("num3: "))
num3: 69
print(f("Total sum: {a,b,c}"))
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    print(f("Total sum: {a,b,c}"))
NameError: name 'f' is not defined
print(f("Total sum: {a+b+c}"))
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    print(f("Total sum: {a+b+c}"))
NameError: name 'f' is not defined
print("Total sum: {a,b,c}")
Total sum: {a,b,c}
print("Total sum: {a+b+c}")
Total sum: {a+b+c}




#Q.10 Take an input from user & make a task
#A simple string trick: REverse whatever the user types
user_input = input("Enter a word to see a trick:")
Enter a word to see a trick:Wingardium Leviosa!
print(f"Wingardium leviosa!") Your word\backwards is:{user_input[::-1]}")
SyntaxError: invalid syntax
print(f"Wingardium leviosa!") word\backwards is:{user_input[::-1]}")
SyntaxError: unexpected character after line continuation character
print(f"Wingardium leviosa!") word is:{user_input[::-1]}")
SyntaxError: unterminated string literal (detected at line 1)
print(f"Wingardium leviosa1!") word\backwards is:{user_input[::-1]}")
SyntaxError: unexpected character after line continuation character
