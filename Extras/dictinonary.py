# 1. Convert list of tuples into a dictionary
lst = [("name", "Elie"), ("job", "Instructor")]
dict1 = {k: v for k, v in lst}
print(dict1)  # {'name': 'Elie', 'job': 'Instructor'}

# 2. Combine two lists into a dictionary using zip
keys = ["CA", "NJ", "RI"]
values = ["California", "New Jersey", "Rhode Island"]
dict2 = {k: v for k, v in zip(keys, values)}
print(dict2)  # {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}

# 3. Create a dictionary with vowels as keys and 0 as value
vowels = "aeiou"
dict3 = {v: 0 for v in vowels}
print(dict3)  # {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# 4. Create a dictionary with position of letters as key and letter as value
dict4 = {i+1: chr(65+i) for i in range(26)}
print(dict4)
# {1: 'A', 2: 'B', 3: 'C', ..., 26: 'Z'}

# 5. Super Bonus: count vowels in a string
s = "awesome sauce"
dict5 = {v: s.count(v) for v in vowels}
print(dict5)  # {'a': 2, 'e': 3, 'i': 0, 'o': 1, 'u': 1}
