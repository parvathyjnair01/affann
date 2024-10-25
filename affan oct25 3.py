temp=float(input("enter the temperature"))
unit=input("enter the unit of c for (c)elcius and f for (f)ahrenheat")
if unit=="c":
    f=(9/5*temp)+32
    print("celcius",f)
else:
    c = 5/9*(temp-32)
    print("fahrenheat",c)


