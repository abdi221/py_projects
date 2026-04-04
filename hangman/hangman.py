import random
list = ['Elephant', 'Tiger', 'Axolotl', 'Platypus', 'Blue Whale', 'Penguin', 'Pangolin', 'Narwhal', 'Honey Badger', 'Glass Frog']

random_word = random.choice(list).lower()
# print(random_word)
# user = input("Guess a letter: ")
# mylist = []
# for i, v in enumerate(random_word.replace(" ", ""), start=1):
#     if user == v:
#         mylist.append(*v)

#     else:
#         mylist.append("_")
# print(" ".join(mylist))

def someword(word):
    thelist = []
    random_word = random.choice(list).lower()
    if word in random_word:
        return thelist.append(word)
    else:
        thelist.append("_")
user = input("Guess a letter")
print(someword(user))


hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


