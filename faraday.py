import math

Q1 = float(input("Enter Q1 charge(in coulombs C): "))
Q2 = float(input("Enter Q2 charge(in coulombs C): "))
R = float(input("Enter the radius ,R (in meters): "))
espsi = 8.854e-12

F = (Q1 * Q2) / (4 * math.pi * espsi * R**2)

print(f"\n The electric force by charges Q1 and Q2 is: {F:.4e} N")

