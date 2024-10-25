num = int(input("enter a number"))
sum_of_digits=0
while num>0:
    reminder = num%10
    sum_of_digits = sum_of_digits+reminder
    number = num//10
print("Sum of digits of the given number:",sum_of_digits)