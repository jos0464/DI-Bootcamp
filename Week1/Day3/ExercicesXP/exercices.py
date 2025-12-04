# ==========================================
# 🐍 Exercises XP
# Last Updated: October 31st, 2025
# ==========================================

# ================================================================
# 🌟 Exercise 1: Converting Lists into Dictionaries
# ================================================================

print("\n--- Exercise 1: Converting Lists into Dictionaries ---")

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Method 1: Using zip()
my_dict = dict(zip(keys, values))
print("Dictionary using zip():", my_dict)

# Method 2: Using dictionary comprehension
my_dict2 = {keys[i]: values[i] for i in range(len(keys))}
print("Dictionary using comprehension:", my_dict2)


# ================================================================
# 🌟 Exercise 2: Cinemax #2
# ================================================================

print("\n--- Exercise 2: Cinemax #2 ---")

family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
total_cost = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    print(f"{name.capitalize()} pays ${price}")
    total_cost += price

print(f"Total cost: ${total_cost}")

# Bonus: Uncomment below to allow user input
"""
family = {}
while True:
    name = input("Enter family member name (or 'stop' to end): ")
    if name.lower() == 'stop':
        break
    age = int(input(f"Enter {name}'s age: "))
    family[name] = age
print(family)
"""


# ================================================================
# 🌟 Exercise 3: Zara
# ================================================================

print("\n--- Exercise 3: Zara ---")

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# 1. Change number of stores
brand["number_stores"] = 2

# 2. Describe Zara's clients
print(f"Zara's clients are {', '.join(brand['type_of_clothes'])}.")

# 3. Add country_creation
brand["country_creation"] = "Spain"

# 4. Add new competitor if key exists
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# 5. Delete creation_date
brand.pop("creation_date")

# 6. Print last competitor
print("Last international competitor:", brand["international_competitors"][-1])

# 7. Major colors in the US
print("Major colors in the US:", brand["major_color"]["US"])

# 8. Number of keys
print("Number of keys in dictionary:", len(brand))

# 9. All keys
print("All keys:", list(brand.keys()))

# Bonus: Merge dictionaries
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

brand.update(more_on_zara)
print("Updated brand dictionary:", brand)


# ================================================================
# 🌟 Exercise 4: Disney Characters
# ================================================================

print("\n--- Exercise 4: Disney Characters ---")

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1. Characters -> indices
dict1 = {user: index for index, user in enumerate(users)}
print("Characters to indices:", dict1)

# 2. Indices -> characters
dict2 = {index: user for index, user in enumerate(users)}
print("Indices to characters:", dict2)

# 3. Alphabetically sorted characters -> indices
sorted_users = sorted(users)
dict3 = {user: index for index, user in enumerate(sorted_users)}
print("Alphabetically sorted characters to indices:", dict3)
