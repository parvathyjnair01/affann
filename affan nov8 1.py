n=int(input("enter the numbers to be inputed"))
num=int(input("enter the number"))
largest=num
smallest=num

while n>1:
    num=int(input("enter number:"))
    if num>largest:
        largest=num
    elif num<smallest:
        smallest=num
    n-=1
    print(f"largest is :{largest}")
    print(f"smallest is :{smallest}")
