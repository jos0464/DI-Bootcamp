import string
import re
from collections import Counter

# =========================
# Part I & II: Text Analysis
# =========================
class Text:
    def __init__(self, text):
        self.text = text

    # Count occurrences of a specific word
    def word_frequency(self, word):
        words = self.text.lower().split()
        count = words.count(word.lower())
        if count == 0:
            return f"'{word}' not found in text."
        return count

    # Find the most common word in the text
    def most_common_word(self):
        words = self.text.lower().split()
        if not words:
            return None
        word_counts = Counter(words)
        most_common = word_counts.most_common(1)[0][0]
        return most_common

    # Return unique words as a list
    def unique_words(self):
        words = self.text.lower().split()
        return list(set(words))

    # Class method to create a Text instance from a file
    @classmethod
    def from_file(cls, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            return cls(content)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return cls("")

# =========================
# Bonus: Text Modification
# =========================
class TextModification(Text):
    # Remove all punctuation from text
    def remove_punctuation(self):
        translator = str.maketrans('', '', string.punctuation)
        self.text = self.text.translate(translator)
        return self.text

    # Remove stop words from text
    def remove_stop_words(self):
        stop_words = {
            "a", "an", "the", "and", "or", "but", "if", "while", "with",
            "is", "was", "for", "on", "in", "at", "by", "to", "of", "from",
            "as", "are", "be", "this", "that", "these", "those", "it"
        }
        words = self.text.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        self.text = " ".join(filtered_words)
        return self.text

    # Remove special characters (non-alphanumeric, except spaces)
    def remove_special_characters(self):
        self.text = re.sub(r'[^A-Za-z0-9\s]', '', self.text)
        return self.text

# =========================
# Example Usage
# =========================
if __name__ == "__main__":
    sample_text = "Hello! This is a sample text. Hello world, hello Python."
    
    # Create a Text instance
    t = Text(sample_text)
    print("Word frequency of 'hello':", t.word_frequency("hello"))
    print("Most common word:", t.most_common_word())
    print("Unique words:", t.unique_words())

    # Create Text instance from file
    # t_file = Text.from_file("example.txt")  # Uncomment if you have a file

    # Text modification
    tm = TextModification(sample_text)
    print("Remove punctuation:", tm.remove_punctuation())
    print("Remove stop words:", tm.remove_stop_words())
    print("Remove special characters:", tm.remove_special_characters())
