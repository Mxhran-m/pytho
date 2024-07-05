#Lab2 progratn to solve quadratic equation
import math
a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))
discriminant = b**2 -4*a*c
if discriminant > 0:
    rootl = (-b + math.sqrt(discriminant))/(2*a)
    root2 = (-b - math.sqrt(discriminant))/(2*a)
    print("The equation has two real roots:",rootl,"and",root2)
elif discriminant == 0:
    root=-b/(2*a)
    print("The equation has one real root:", root)
else:
    print("does not have a real root")
