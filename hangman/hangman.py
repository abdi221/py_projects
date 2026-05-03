import random
def hangman():
  hangmanpics = [r''' #adding r tells the interpreter to look at the figures as they are seen and not new lines
    +---+
    |   |
        |
        |
        |
        |
  =========''', r'''
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', r'''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', r'''
    +---+
    |   |
    O   |
  /|   |
        |
        |
  =========''', r'''
    +---+
    |   |
    O   |
  /|\  |
        |
        |
  =========''', r'''
    +---+
    |   |
    O   |
  /|\  |
  /    |
        |
  =========''', r'''
    +---+
    |   |
    O   |
  /|\  |
  / \  |
        |
  =========''']

list = ['Elephant', 'Tiger', 'Axolotl', 'Platypus', 'Blue Whale', 'Penguin', 'Pangolin', 'Narwhal', 'Honey Badger', 'Glass Frog']

random_word = random.choice(list).lower()
print(random_word)

def someword(word):
  mylist = [] # this stores my letters in order
  for i, v in enumerate(random_word.replace(" ", ""), start=1):
      print("_" * i) # hopefully this would print _ _ _ at the start of the program
      if word == v:
        mylist.append(*word)
      else:
        shieet = i * "_"
        mylist.append(shieet)
  return " ".join(mylist)

def main():
  hangman()
  guess = 0 #ei amount of tries
  all_guessed_words = {*()} #set because its smarter and it doesnt care about the order
  while guess <= len(random_word) + 2:  
    letter = input("Guess a letter")
    all_guessed_words.add(letter)
    guess += 1
    if letter not in random_word:
      print(hangman())
