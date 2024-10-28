while True:
    print("\n1.\tConvert Celsius to Fahrenheit")
    print("2.\tConvert Fahrenheit to Celsius")
    print("3.\tExit the program")
    choice=float(input("choose a choice:"))
    if choice==1:
        temp = float(input("enter the temperature in celsius"))
        tempc = (9/5*temp)+32
        print("The equivalent Temperature in fahrenheit is:",tempc)
    elif choice==2:
        temp = float(input("enter the temperature in Fahrenheit"))
        tempf = (9/5*temp)+32
        print("The equivalent Temperature in fahrenheit is:", tempf)
    elif choice==3:
        break
    else:
        print("invalid entry")


