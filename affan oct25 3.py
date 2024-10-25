temp=float(input("enter the temperature"))
unit=input("enter the unit of c for celcius and f for fahrenheat")
if unit=="c":
 c=(temp-32)*5/9
 print("celcius",c)
else:
 f=(temp*9/5)+32
 print("fahrenheat",f)


