# ===============================================
#              Python XP Exercises
# ===============================================

# Exercise 1: Favorite Numbers
print("\n🌟 Exercise 1: Favorite Numbers")
my_fav_numbers = {3, 7, 21}  # tes nombres favoris
my_fav_numbers.add(42)
my_fav_numbers.add(17)
my_fav_numbers.remove(17)

friend_fav_numbers = {5, 11, 21}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)


# Exercise 2: Tuple
print("\n🌟 Exercise 2: Tuple")
my_tuple = (1, 2, 3)
my_tuple = my_tuple + (4, 5)  # créer un nouveau tuple pour "ajouter"
print("Updated tuple:", my_tuple)


# Exercise 3: List Manipulation
print("\n🌟 Exercise 3: List Manipulation")
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print("Count of Apples:", basket.count("Apples"))
basket.clear()
print("Final basket:", basket)


# Exercise 4: Floats
print("\n🌟 Exercise 4: Floats")
numbers = [x * 0.5 for x in range(3, 11)]  # 1.5, 2, 2.5 ... 5
print("Generated sequence:", numbers)


# Exercise 5: For Loop
print("\n🌟 Exercise 5: For Loop")
print("Numbers 1-20:")
for i in range(1, 21):
    print(i, end=" ")
print("\nEven numbers 1-20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")
print()


# Exercise 6: While Loop
print("\n🌟 Exercise 6: Name Validation")
while True:
    name = input("Enter your name: ")
    if not name.isdigit() and len(name) >= 3:
        print("Thank you")
        break
    else:
        print("Please enter a valid name (at least 3 letters, not digits).")


# Exercise 7: Favorite Fruits
print("\n🌟 Exercise 7: Favorite Fruits")
fruits = input("Enter your favorite fruits (separated by spaces): ").split()
choice = input("Pick a fruit: ")
if choice in fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")


# Exercise 8: Pizza Toppings
print("\n🌟 Exercise 8: Pizza Toppings")
toppings = []
while True:
    topping = input("Enter a topping (type 'quit' to stop): ")
    if topping.lower() == "quit":
        break
    print(f"Adding {topping} to your pizza.")
    toppings.append(topping)
total_cost = 10 + len(toppings) * 2.5
print("Toppings:", toppings)
print("Total cost: $", total_cost)


# Exercise 9: Cinemax Tickets
print("\n🌟 Exercise 9: Cinemax Tickets")
ages_input = input("Enter ages of family members separated by spaces: ").split()
ages = [int(age) for age in ages_input]
total = 0
for age in ages:
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    total += price
print("Total ticket cost: $", total)

# Bonus: restricted movie 16-21
print("\nBonus: Restricted movie (16-21)")
group_input = input("Enter ages of attendees separated by spaces: ").split()
group = [int(age) for age in group_input]
allowed = [age for age in group if 16 <= age <= 21]
print("Allowed attendees:", allowed)
