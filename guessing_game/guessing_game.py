from random import randint

computer = randint(1, 10) #stores the computers value
print("Guess between 1 and 100 included\n")
count = 0 # stores count values so we can end the loop if 
while True:
    user = int(input("Guess the number: "))
    if user == computer and count <= 4:
        print(f"You guessed it correctly! And under 3 tries!! The correct number was {computer}")
        break
    count += 1
    if count == 5:
        print(f"Out of tries and not guessed correcly. {count} of 5")
        break
    elif user < computer:
        print(f"Wrong Guess. Too low. Tries {count} of 5")
    else:
        print(f"Wrong Guess. Too high. Tries {count} of 5")
