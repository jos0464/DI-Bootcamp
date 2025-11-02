import random

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 7 attempts to guess it correctly.\n")

secret_number = random.randint(1, 100)

attempts = 7

for attempt in range(1, attempts + 1):
    try:
        guess = int(input(f"Attempt {attempt}/{attempts} - Enter your guess: "))
    except ValueError:
        print("❌ Please enter a valid number!")
        continue

    if guess < secret_number:
        print("📉 Too low! Try a higher number.\n")
    elif guess > secret_number:
        print("📈 Too high! Try a lower number.\n")
    else:
        print(f"🎉 Congratulations! You guessed it in {attempt} attempts!")
        break
else:
    # Only runs if the loop didn't break (i.e., player failed)
    print(f"😢 Sorry, you’ve used all {attempts} attempts.")
    print(f"The correct number was {secret_number}.")

print("👋 Thanks for playing!")
