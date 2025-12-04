# =========================
# Exercices XP - Python
# Regroupés dans un seul fichier
# =========================

# =========================
# Exercise 1: Random Sentence Generator
# =========================
import random
import sys
import json
import string
from datetime import datetime, timedelta
from faker import Faker

# Function to read words from a file
def get_words_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            words = content.split()
            return words
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

# Function to generate a random sentence
def get_random_sentence(sentence_length, file_path="words.txt"):
    words = get_words_from_file(file_path)
    sentence_words = [random.choice(words).lower() for _ in range(sentence_length)]
    sentence = " ".join(sentence_words)
    return sentence

# Main function for sentence generator
def random_sentence_main():
    print("=== Random Sentence Generator ===")
    try:
        length = int(input("Enter sentence length (2-20): "))
        if not 2 <= length <= 20:
            print("Error: Length must be between 2 and 20.")
            return
    except ValueError:
        print("Error: Enter a valid integer.")
        return
    sentence = get_random_sentence(length)
    print("Generated sentence:", sentence)

# =========================
# Exercise 2: Working with JSON
# =========================
def json_exercise():
    sampleJson = """{ 
       "company":{ 
          "employee":{ 
             "name":"emma",
             "payable":{ 
                "salary":7000,
                "bonus":800
             }
          }
       }
    }"""
    data = json.loads(sampleJson)

    # Access nested salary
    salary = data["company"]["employee"]["payable"]["salary"]
    print("Salary:", salary)

    # Add birth_date key
    data["company"]["employee"]["birth_date"] = "1990-05-15"

    # Save modified JSON
    with open("modified_employee.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Modified JSON saved to 'modified_employee.json'.")

# =========================
# Exercise 3: Currencies
# =========================
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}s"

    __repr__ = __str__

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        elif isinstance(other, (int, float)):
            return self.amount + other
        else:
            raise TypeError("Unsupported type for addition")

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        elif isinstance(other, (int, float)):
            self.amount += other
        else:
            raise TypeError("Unsupported type for addition")
        return self

# =========================
# Exercise 4: String and Random
# =========================
def random_string(length=5):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# =========================
# Exercise 5: Current Date
# =========================
def show_current_date():
    today = datetime.now()
    print("Current date:", today.strftime("%Y-%m-%d"))

# =========================
# Exercise 6: Time until Jan 1
# =========================
def time_until_jan1():
    now = datetime.now()
    next_year = datetime(year=now.year + 1, month=1, day=1)
    diff = next_year - now
    print("Time until January 1st:", diff)

# =========================
# Exercise 7: Minutes lived since birthday
# =========================
def minutes_lived(birthdate_str, date_format="%Y-%m-%d"):
    birthdate = datetime.strptime(birthdate_str, date_format)
    now = datetime.now()
    diff = now - birthdate
    minutes = int(diff.total_seconds() / 60)
    print(f"You have lived {minutes} minutes.")

# =========================
# Exercise 8: Faker module - fake users
# =========================
def generate_fake_users(n):
    fake = Faker()
    users = []
    for _ in range(n):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        users.append(user)
    return users

# =========================
# Exercise 9: Circle class
# =========================
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius {self.radius}"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

# =========================
# Example usage of functions
# =========================
if __name__ == "__main__":
    # Random sentence
    # random_sentence_main()
    
    # JSON exercise
    json_exercise()
    
    # Currency exercise
    c1 = Currency('dollar', 5)
    c2 = Currency('dollar', 10)
    c1 += 5
    c1 += c2
    print(c1)
    
    # Random string
    print("Random string:", random_string())
    
    # Current date
    show_current_date()
    
    # Time until Jan 1
    time_until_jan1()
    
    # Minutes lived
    minutes_lived("1990-01-01")
    
    # Generate fake users
    users = generate_fake_users(3)
    print("Fake users:", users)
    
    # Circle examples
    cA = Circle(5)
    cB = Circle(3)
    print("Circle area:", cA.area())
    cC = cA + cB
    print(cC)
