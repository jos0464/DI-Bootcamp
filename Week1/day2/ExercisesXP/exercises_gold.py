# ===============================================
#           Exercises XP Gold - Console Version
#           ASCII only, Windows safe
# ===============================================

import random

# Exercise 1: Concatenate lists
print("* Exercise 1: Concatenate lists")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1.copy()
combined.extend(list2)
print(f"Combined list: {combined}\n")

# Exercise 2: Range of numbers (résumé)
print("* Exercise 2: Range of numbers")
multiples = [i for i in range(1500, 2501) if i % 5 == 0 and i % 7 == 0]
print(f"Number of multiples of 5 and 7: {len(multiples)}")
print(f"First 10 multiples: {multiples[:10]}\n")

# Exercise 3: Check the index
print("* Exercise 3: Check the index")
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("Enter your name: ")
if user_name in names:
    idx = names.index(user_name)
    print(f"{user_name} is at index {idx}\n")
else:
    print(f"{user_name} not found in the list.\n")

# Exercise 4: Greatest Number
print("* Exercise 4: Greatest Number")
nums = []
for i in range(1, 4):
    num = int(input(f"Input the {i} number: "))
    nums.append(num)
greatest = max(nums)
print(f"The greatest number is: {greatest}\n")

# Exercise 5: The Alphabet
print("* Exercise 5: The Alphabet")
alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
for letter in alphabet:
    if letter in vowels:
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is a consonant")
print()

# Exercise 6: Words and letters
print("* Exercise 6: Words and letters")
words = [input(f"Enter word {i+1}: ") for i in range(7)]
letter = input("Enter a single letter: ")
for word in words:
    if letter in word:
        idx = word.index(letter)
        print(f"In word '{word}', letter '{letter}' first occurs at index {idx}")
    else:
        print(f"Letter '{letter}' not found in word '{word}'")
print()

# Exercise 7: Min, Max, Sum (résumé)
print("* Exercise 7: Min, Max, Sum")
numbers = list(range(1, 1000001))
print(f"Min: {min(numbers)}, Max: {max(numbers)}, Sum: {sum(numbers)}\n")

# Exercise 8: List and Tuple
print("* Exercise 8: List and Tuple")
seq_input = input("Enter comma-separated numbers: ")
num_list = seq_input.split(",")
num_tuple = tuple(num_list)
print(f"List: {num_list}\nTuple: {num_tuple}\n")

# Exercise 9: Random number
print("* Exercise 9: Random number")
wins, losses = 0, 0
while True:
    user_input = input("Guess a number from 1 to 9 (or 'quit' to stop): ")
    if user_input.lower() == "quit":
        break
    if not user_input.isdigit() or not 1 <= int(user_input) <= 9:
        print("Invalid input, try again.")
        continue
    user_guess = int(user_input)
    rand_num = random.randint(1, 9)
    if user_guess == rand_num:
        print("Winner!")
        wins += 1
    else:
        print("Better luck next time.")
        losses += 1
print(f"Total games won: {wins}, Total games lost: {losses}")
