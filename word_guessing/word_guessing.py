import random
list = ['elephant', 'tiger', 'axolotl', 'platypus', 'blue whale', 'penguin', 'pangolin', 'narwhal', 'honey badger', 'glass frog']
# print(*random.choice(l)) 

# NOTE: for later remeber to maybe use sample() for unique non duplicate values..

# NOTE: use enumerate for better indexing method!! ↓ this ↓↓↓↓↓

comp_word = random.choice(list) # this picks a random word (whole word) from the list
print(comp_word)
new_list = []
count = 0 # to keep count
while count < 6:
    for i in comp_word:
        user = input("Guess a letter: ")
        count += 1
        if user in comp_word:
            new_list.append(i)
        else:
            new_list.append('_')
        # if count == 6:
        #     print("out of tries\n")
        break
print("Here is the words you tried out:")
print(*new_list, end="")
print()