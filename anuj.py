def show_balance():
    print(f"Your current balance is ${balance:.2f}")
def deposit():
    amount=float(input("Enter the amount you want to deposit in your bank account:"))
    if amount<0:
        print("Deposit cannot be in negative")
        return 0
    elif amount==0:
        print("Deposit should be greater than zero")
        return 0
    else:
        return amount
def withdraw():
    money=float(input("Enter the amount you want to withdraw"))
    if money==0:
        print("zero cant be withdrawn")
        return 0
    elif money<0:
        print("Negative amount cant be withdrawn")
        return 0
    else:
        print("Successfully withdrawn!")
        return money
is_running=True
balance=0
while is_running:
    print("Banking program")
    print("1-Show Balance")
    print("2-Deposit")
    print("3-Withdraw")
    print("4-Exit")
    print()
    choice=input("choose between (1-4) to define your purpose:")
    if choice=="1":
        show_balance()
    if choice=="2":
        balance+=deposit()    
    if choice=="3":
        returned_valueafterwithdraw=withdraw()
        balance-=returned_valueafterwithdraw
        if returned_valueafterwithdraw>0:
            print(f"The remaining amount in your account is ${balance:.2f}")
    if choice=="4":
        is_running=False
print("Thankyou for using our service!")                        