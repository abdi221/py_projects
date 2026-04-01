# document: created 10 animals from a list and printed one randomly
# Then I created a loop which would take a random animal from my list and printing each letter one at a time
import random
list = ['elephant', 'tiger', 'axolotl', 'platypus', 'blue whale', 'penguin', 'pangolin', 'narwhal', 'honey badger', 'glass frog']
l = ['elephant', 'tiger', 'axolotl']
# print(*random.choice(l)) 

# NOTE: for later remeber to maybe use sample() for unique non duplicate values..
for letter in l: # now i can see that by using the 'in' keyword, i can search for single letter in the word
    print(letter)
    if "a" in letter:
        print("Yes")
    else:
        print("No")