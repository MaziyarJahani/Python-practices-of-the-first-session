name = input ("Please write down your full name:")
a = int (input ("Please enter your grade in the first course:"))
b = int (input ("Please enter your grade in the second course:"))
c = int (input ("Please enter your grade in the third course:"))
if a > 20 or b > 20 or c > 20 or a or b or c < 0:
    print("koja dars mikhooni?")
else:
    average = (a + b + c)/3
    if average>17:
        print("Hi", name , ", Your average is Great.")
    if 17>average>12:
        print("Hi", name , ", Your average is normal.")
    if average < 12:
        print("Hi", name , ", You Failed.")