import random
txt = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''


user = input("Guess letter: ")
t = 'a b c'.split()
for letter in t:
    if user == letter:
        print(letter, end=" ")
    else:
        print("_", end=" ")
print()