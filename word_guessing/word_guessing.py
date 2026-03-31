from random import choice
#list = ["hello", "welcome", "random", "file", "print", "tracking", "word", "tasks", "concepts", "core"]

# word = choice(list)
# count = 0
# print("You got 10 tries\n")
# for letter in range(len(word.lower())):
#     user = input("Guess the first letter of the word: ")
#     if user.lower() == letter:
#         print(letter, end="")
#     else:
#         print("_", end="")
#     count += 1
#     if count == 10:
#         print("Game Over. You Lost")

# print()
#problem: the iterator is jumping over a letter if not guessed correctly within the sequence
word = 'apple'
lists = []
for i in word:
    user = input("Guess a letter: ")
    if user in word:
        print(f"Yes the letter {user} is in the word.")
        lists.append(i)
    else:
        print(f"No the letter {user} is not in the word")

print(lists)
