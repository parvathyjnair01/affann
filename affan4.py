'''
Authore: affan muhammed
Date: 18-10-2024
Description: Write a Python program that uses functions from the math module to perform the following operations on a number provided by the user:
    Find the square root.
    Calculate the factorial.
    Raise the number to the power of 2.
'''


import math
number=int(input("Enter a number:"))
Square_root=math.sqrt(number)
print("Square root of ",number,":",Square_root)
Factorial=math.factorial(number)
print("Factorial of ",number,":",Factorial)
Power=math.pow(number,2)
print(number,"raised to power 2",Power)