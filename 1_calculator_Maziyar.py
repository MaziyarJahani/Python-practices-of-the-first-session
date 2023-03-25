import math
print ("Welcome to my caclculator")
print ("Please enter you'r choice")
print ("+ : sum , - : sub , * : mul , / : div , sin , cos , tan , cot , log , √ : sqrt , ! : factorial ")
op= input()
if op == "+" or op == "-" or op == "*" or op == "/":
    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0 : 
                result=" Can't divide by zero"
        else:
                result = a / b
if op == "√":
    print("The second number is considered as the root.")
    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
    if a<0:
        result = "I can't take roots from negative numbers"
    elif b == 0:
        result= "Undefined"
    else:
        result = a ** (1/b)
if op == "sin" or op == "cos" or op == "tan" or op == "cot" or op == "log":
    a = float(input("Enter your number:"))
    rad = (a * math.pi) / 180
    if op == "sin":
        result= math.sin(rad)
    if op == "cos":
        result= math.cos(rad)
    if op == "tan":
        result= math.tan(rad)
    if op == "cot":
        result= math.cot(rad)
    if op == "log":
        result= math.log(a)
if op == "!":
    a = int(input("Enter your number:"))
    result= math.factorial(a)
print (result)