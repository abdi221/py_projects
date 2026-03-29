balance = 1000


def withdraw():
    global balance #so you dont start with the same balance every time
    print(f"Remaning funds: {balance}\n")
    print("How much do you like to withdraw?\n")
    user = int(input("Enter amount to withdraw  or press 0 to exit: "))

    if user == 0: # if user enters 0 then the withdraw action ends
        return
    if user > balance: # check if user entered too much money 
        print("Unsufficient amount")
    balance -= user
    print("\nAmount Left:", balance)
    

def seeBal():
    print(balance)

def deposit():
    global balance
    user = int(input("Enter amount to deposit or press 0 to exit: "))
    if user == 0: # same here; if user enters 0 the deposit action ends - preventing infinit loop
        return
    balance += user
    print(f"Balance: {balance}")

        
def exitprogram():
    print("Goodbye\n")
    

def main():
    print("\n1. See balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    while True:
        choice = int(input("Choose from 1 to 4: "))
        if choice > 4:
            print("Invalid choice")
            exit()
        elif choice == 1:
            seeBal()
        elif choice == 2:
            deposit()
            
        elif choice == 3:
            withdraw()
        elif choice == 4:
            exitprogram()
            break

main()