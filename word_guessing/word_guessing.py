import random
list = ['elephant', 'tiger', 'axolotl', 'platypus', 'blue whale', 'penguin', 'pangolin', 'narwhal', 'honey badger', 'glass frog']

# NOTE: for later remeber to maybe use sample() for unique non duplicate values..

# NOTE: use enumerate for better indexing method!! ↓ this ↓↓↓↓↓

random_word = random.choice(list).replace(" ", "")
user = input("Guess a letter: ")
letter_count = 0
for i in random_word:
    if user == i:
        letter_count += 1
try:
    letter_count > 0
    print(f"The letter {user} appears {letter_count} times in {random_word}")
except:
    print(f"The letter {user} appears {letter_count} times in {random_word}")