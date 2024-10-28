balance_amount=1000
while True:
    print("\n1.\tCheck Balance")
    print("2.\tDeposit Money")
    print("3.\tWithdraw Money")
    print("4.\tExit")
    choice= int(input("Enter your choice:"))
    if choice==1:
        print(f"the current balance ${balance_amount}")
    elif choice==2:
        deposit_amount=float(input("enter the amount"))
        balance_amount=balance_amount + deposit_amount
        print(f"the deposit amount ${deposit_amount}and the current balance ${balance_amount}")
    elif choice==3:
        withdraw_amount=float(input("enter the amount to withdraw"))
        if balance_amount<withdraw_amount:
            print(f"insufficient balance")
        else:
         balance_amount=balance_amount - withdraw_amount
         print(f"the withdraw amount ${withdraw_amount}and the current balance ${balance_amount}")

    elif choice==4:
        break
    else:
        print("invalid entry")

