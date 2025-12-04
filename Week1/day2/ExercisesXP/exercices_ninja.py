# ===============================================
#           Exercises: Lists, Tuples, Loops
#           Console Version - Windows Safe
# ===============================================

import math
import random

# ================= Exercise 1: Formula =================
print("* Exercise 1: Formula")

C = 50
H = 30
user_input = input("Enter comma-separated numbers: ")
numbers = user_input.split(",")
results = []

for D in numbers:
    try:
        D = int(D)
        Q = math.sqrt((2 * C * D) / H)
        results.append(str(int(Q)))  # convertir en int pour afficher comme 18,22,24
    except ValueError:
        print(f"Invalid number: {D}")

print("Results:", ",".join(results))
print()

# ================= Exercise 2: List of integers =================
print("* Exercise 2: List of integers")

# Option: predefined list
nums = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]

print("Original list:", nums)
print("Sorted descending:", sorted(nums, reverse=True))
print("Sum:", sum(nums))
print("First and last:", [nums[0], nums[-1]])
print("Numbers greater than 50:", [x for x in nums if x > 50])
print("Numbers smaller than 10:", [x for x in nums if x < 10])
print("Numbers squared:", [x**2 for x in nums])
unique_nums = list(set(nums))
print("Unique numbers:", unique_nums)
print("Count of unique numbers:", len(unique_nums))
print("Average:", sum(nums)/len(nums))
print("Largest number:", max(nums))
print("Smallest number:", min(nums))

# Bonus: manual sum, average, largest, smallest
total = 0
largest = nums[0]
smallest = nums[0]
for x in nums:
    total += x
    if x > largest:
        largest = x
    if x < smallest:
        smallest = x
average = total / len(nums)
print("Manual sum:", total)
print("Manual average:", average)
print("Manual largest:", largest)
print("Manual smallest:", smallest)
print()

# Bonus: user input 10 numbers
user_nums = []
print("Enter 10 integers between -100 and 100:")
for i in range(10):
    while True:
        try:
            n = int(input(f"Number {i+1}: "))
            if -100 <= n <= 100:
                user_nums.append(n)
                break
            else:
                print("Number must be between -100 and 100")
        except ValueError:
            print("Invalid input, try again")
print("User numbers:", user_nums)
print()

# Bonus: generate random integers
rand_nums = [random.randint(-100,100) for _ in range(10)]
print("Random numbers:", rand_nums)

# Bonus: random amount of integers (>=50)
amount = random.randint(50, 100)
rand_list = [random.randint(-100,100) for _ in range(amount)]
print(f"Random list of {amount} numbers generated\n")

# ================= Exercise 3: Working on a paragraph =================
print("* Exercise 3: Paragraph analysis")
paragraph = """Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."""

# Basic stats
chars = len(paragraph)
sentences = paragraph.count('.') + paragraph.count('!') + paragraph.count('?')
words = paragraph.split()
unique_words = set(words)
non_whitespace_chars = len(paragraph.replace(" ", ""))
avg_words_per_sentence = len(words)/sentences
non_unique_count = len(words) - len(unique_words)

print("Number of characters:", chars)
print("Number of sentences:", sentences)
print("Number of words:", len(words))
print("Number of unique words:", len(unique_words))
print("Non-whitespace characters:", non_whitespace_chars)
print("Average words per sentence:", round(avg_words_per_sentence,2))
print("Number of non-unique words:", non_unique_count)
print()

# ================= Exercise 4: Frequency of words =================
print("* Exercise 4: Frequency of words")
text = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
words_list = text.split()
freq = {}

for w in words_list:
    freq[w] = freq.get(w,0) + 1

for k,v in sorted(freq.items()):
    print(f"{k}:{v}")
