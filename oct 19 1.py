"""Simple desktop calculator using Python. Only the five basic arithmetic operators.

AIM: Write a Python program that performs the following tasks:"""
num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
num3 = int(input("enter the third number:"))
sum = num1+num2
print("The sum of num1 and num2 is:",sum)
difference =num2-num1
print("The difference when num2 is subtracted from num1 is:",difference)
multiply = num1*num2
print("The product of num1 and num2 is:",multiply)
divide = num1/num2
print("The quotient when num1 is divided by num2 is:",divide)
modulus = num1%num2
print("The remainder when num1 is divided by num2 is:", modulus)
result = (num1 + num2) * num3 / 2
print("The result of (num1 + num2) * num3 / 2 is:", result)