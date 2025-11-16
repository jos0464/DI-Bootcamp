# 1. Print all values in the list
lst1 = [1, 2, 3, 4]
print([x for x in lst1])  # [1, 2, 3, 4]

# 2. Print all values multiplied by 20
print([x * 20 for x in lst1])  # [20, 40, 60, 80]

# 3. First letter of each name
names = ["Elie", "Tim", "Matt"]
print([name[0] for name in names])  # ['E', 'T', 'M']

# 4. Even values from list
lst2 = [1, 2, 3, 4, 5, 6]
print([x for x in lst2 if x % 2 == 0])  # [2, 4, 6]

# 5. Intersection of two lists
lst3 = [1, 2, 3, 4]
lst4 = [3, 4, 5, 6]
print([x for x in lst3 if x in lst4])  # [3, 4]

# 6. Reverse each word and convert to lower case
print([word[::-1].lower() for word in names])  # ['eile', 'mit', 'ttam']

# 7. Letters present in both strings
str1 = "first"
str2 = "third"
print([c for c in str1 if c in str2])  # ['i', 'r', 't']

# 8. Numbers divisible by 12 between 1 and 100
print([x for x in range(1, 101) if x % 12 == 0])  # [12, 24, 36, 48, 60, 72, 84, 96]

# 9. Remove vowels from string
s = "amazing"
vowels = "aeiou"
print([c for c in s if c not in vowels])  # ['m', 'z', 'n', 'g']

# 10. Generate [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
print([[x for x in range(3)] for _ in range(3)])  # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

result = [[x for x in range(10)] for _ in range(10)]
for row in result:
    print(row)



# 11. (You didn't specify the last one completely)
# For example, generate [[0,1,2,3],[0,1,2,3],[0,1,2,3]]
print([[x for x in range(4)] for _ in range(3)])  # Example: [[0,1,2,3],[0,1,2,3],[0,1,2,3]]
