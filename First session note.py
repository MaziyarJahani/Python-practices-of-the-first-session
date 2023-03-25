print("hello world")
print("hello sajjad")
name = "Maziyar"
family = "Jahani"
city= "Mashhad"
print("Hello, i'm", name, family, "and i'm living in", city)
#"" prints what is inside of it, in this code, name shouldn't be inside of ""
a= 5
b= 7
c=a*b
print(a+b, c)
#in all programms: input, process, output
name2= input("please enter your name:")
family2= input("please enter your family name:")
city2= input ("please enter your city:")
country= "Iran"
print("Hello", name2, family2, "from", city2,",", country)
d= int(input("enter first number:"))
e= int(input("enter second number:"))
f= d+e
#int makes number out of a string
print(f)
cm= int(input("please enter length of sth in centimeters:"))
inch= cm/2.54
print("your length in inch is:", inch)
centigrade= int(input("please enter T in centigrade"))
Fahrenheit= centigrade * 9 / 5 + 32
print("your Temperature in Fahrenheit is:", Fahrenheit)
#this is a test to see difference between c and C
C=4
print(c)
width= int(input())
height= int(input())
A= width * height
P=(width + height) * 2
print(A)
print(P)
#(()) () ^** * / // % +
r= int(input())
A2= 3.14*r**2
P2= 3.14*r*2
print(A2, P2)
#math library
import math
print(math.pi)
A3= math.pi * r **2
P3= math.pi * r * 2
print ("by using math library, your A and P is:", A3, P3)
#you can also use float instead of int.
import math
a4 = float(input("enter first number:"))
b4 = float(input("enter second number:"))
if a4 > b4:
    print (a4)
else:
    print(b4)
score1= float(input())
score2= float(input())
score3= float(input())
average = (score1 + score2 + score3)/3
print(average)
if average < 12:
    print("mashroot shodi bro")
# Tab: code goes slightly further.