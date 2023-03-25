a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))

if a + b > c and b + c > a and a + c > b:
    print("A triangle with these sides can be formed.")
else:
    print("A triangle with these sides cannot be formed.")