# Exercise 4 : How many characters in a sentence ?
# Instructions:
# Use python to find out how many characters are in the following text.

my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco
laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit
esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum."""

print("Number of characters:", len(my_text))


# Exercise 5: Longest word without a specific character
# Instructions:
# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.

longest_sentence = ""

while True:
    sentence = input("Enter a sentence without the letter 'A' (or type 'quit' to stop): ")

    if sentence.lower() == "quit":
        print("Exiting program. Your longest valid sentence was:")
        print(longest_sentence)
        break

    if "a" in sentence.lower():
        print("That sentence contains an 'A'! Try again.")
    elif len(sentence) > len(longest_sentence):
        longest_sentence = sentence
        print("Congratulations! New longest sentence recorded!")
    else:
        print("Nice try, but it's not longer than your current record.")