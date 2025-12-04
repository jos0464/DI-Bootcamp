# Exercise 1: Hello World
# Print the following output using one line of code:
# Hello world
# Hello world
# Hello world
# Hello world

print("Hello world\n" * 4)


# Exercise 2: Some Math
# Write code that calculates the result of: (99^3)*8

result = (99 ** 3) * 8
print(result)


# Exercise 3: What is the output?
# Predict the output of the following code snippets, then check by running.
# >>> 5 < 3       # False
# >>> 3 == 3      # True
# >>> 3 == "3"    # False
# >>> "3" > 3     # Error (can't compare string and int)
# >>> "Hello" == "hello"  # False

print(5 < 3)
print(3 == 3)
print(3 == "3")
# print("3" > 3)  # This line will cause an error
print("Hello" == "hello")


# 🌟 Exercise 4: Your computer brand
computer_brand = "HP"
print(f"I have a {computer_brand} computer.")


# 🌟 Exercise 5: Your information
name = "Joseph"
age = 59
shoe_size = 42
info = f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}."
print(info)


# 🌟 Exercise 6: A & B
a = 10
b = 5
if a > b:
    print("Hello World")


# Exercise 7: Odd or Even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 🌟 Exercise 8: What’s your name?
user_name = input("What is your name? ")
if user_name.lower() == "joseph":
    print("Hey! We have the same name 😄")
else:
    print(f"Nice to meet you, {user_name}!")


# 🌟 Exercise 9: Tall enough to ride a roller coaster
height = int(input("Enter your height in cm: "))
if height > 145:
    print("You are tall enough to ride 🎢")
else:
    print("You need to grow a bit more to ride!")
