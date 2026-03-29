from random import randint

computer = randint(1, 10) #stores the computers value
print("Guess between 1 and 100 included\n")
count = 0 # stores count values so we can end the loop if 
while True:
    user = int(input("Guess the number: "))
    if user == computer and count <= 4:
        print(f"You guessed it correctly! And under 3 tries!! The correct number was {computer}")
        break
    elif user < computer:
        count += 1
        print(f"Wrong Guess. Too low. Tries {count} of 5")
    elif user > computer:
        count += 1
        print(f"Wrong Guess. Too high. Tries {count} of 5")
    elif count == 5:
        print("Out of tries and not guessed correctly")
        break
    else:
        print("Not a valid input or logic is flawed")