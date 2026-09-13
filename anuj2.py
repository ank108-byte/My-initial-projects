import random
def spin_row():
    symbols=["🍒", "🍉", "🍋", "🔔", "⭐"]
    return [random.choice(symbols) for x in range(3)]
def row(selrow):
    print("**************")
    print(" | ".join(selrow))
    print("**************")
def prize(selrow,bet):
    if selrow[0]==selrow[1]==selrow[2]:
        if selrow[0]=="🍒":
            return bet*2
        if selrow[0]=="🍉":
            return bet*3   
        if selrow[0]=="🍋":
            return bet*4
        if selrow[0]=="🔔":
            return bet*5             
        if selrow[0]=="⭐":
            return bet*10
    return 0
def main():
    amount=1000
    print("*****************************")
    print("Python slots:🍒 🍉 🍋 🔔 ⭐")
    print("*****************************")
    while amount>0:
        print(f"Your current balance is ${amount}")
        bet=input("Enter your bet for the round:")  
        if not bet.isdigit():
            print("Invalid bet")
            continue
        bet=int(bet)
        if bet <= 0:
            print("Bet should be greater than zero to proceed")
            continue
        if bet>amount:
            print("Insufficient fund to spin")
            continue
        amount-=bet
        selrow=spin_row()
        print("Spinning.....\n")
        row(selrow)
        payout=prize(selrow,bet)
        if payout>0:
            print("Congratulations!!!!!")
            print(f"You have won ${payout:.2f}")
        else:
            print("You lost this round")
        amount+=payout
        play_again=input("Do you want to play again(Y/N): ").upper()
        if play_again !="Y":
            break
    print("***************")
    print("Game over!!!!!!")
    print("***************")
    print(f"Your final balance is {amount}")
if __name__=='__main__':
    main()


    
    