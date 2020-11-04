#!user/bin/env python3
import math
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter C:"))
delta = b * b - 4 * a * c
if delta < 0:
    print("ROOTS are imaginary")
else:
    root1 = (-b + math.sqrt(delta)) / (2 * a)
    root2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Root1 = ",root1)
    print("Root2 = ",root2)
