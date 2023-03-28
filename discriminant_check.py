import math
import numbers
import numpy as np
print("This is for checking the discriminant")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if (b*b - 4*a*c) == 0:
    discriminant = (b*b - 4*a*c)
    print(f"The discriminant is equal to : {discriminant}")
    print("The discriminant has one real root ")
elif (b*b - 4*a*c) > 0:
    discriminant = (b*b - 4*a*c)
    print(f"The discriminant is equal to : {discriminant}")
    print("The discriminant has two real roots")
elif (b*b - 4*a*c) < 0:
    discriminant = (b*b - 4*a*c)
    print(f"The discriminant is equal to : {discriminant}")
    print("The discriminant has no real roots ")
