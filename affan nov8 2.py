n=int(input("enter the numbers to be inputed"))
num=int(input("enter the number"))
largest=num
second_largest=num
smallest=num
second_smallest=num

while n>1:
    num=int(input("enter number:"))
    if num>largest:
        second_largest=largest
        largest=num
    elif num<smallest:
        second_smallest=smallest
        smallest=num
    n-=1
print(f"largest is :{largest}")
print(f"smallest is :{smallest}")
print(f"second_largest is :{second_largest}")
print(f"second_smallest is :{second_smallest}")
