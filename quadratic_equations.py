import cmath
import math
print("This code solves quadratic equations")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
discriminant = b**2 - 4*a*c

if discriminant<0:
    soln1 = (-b + cmath.sqrt(discriminant))/2*a
    soln2 = (-b - cmath.sqrt(discriminant))/2*a
    print("The eqation has no real roots")
    print(f"The complex roots of the quadratic equation are: {soln1} & {soln2}")


if discriminant==0:
    soln1 = (-b + math.sqrt(discriminant))/2*a
    print("The quadratic equation has one real root")
    print(f"The root of the quadratic equation is: {soln1} ")
elif discriminant >0:
    soln1 = (-b + math.sqrt(discriminant))/2*a
    soln2 = (-b - math.sqrt(discriminant))/2*a
    print("The quadratic equation has two real roots")
    print(f"The roots of the quadratic equation are : {soln1} & {soln2}")