class AnagramChecker:
    """
    Class used to check valid words and find anagrams.
    """

    def __init__(self, word_list_file="words.txt"):
        """
        Load the word list from the provided file.
        Words are stored in a set for fast lookup.
        """
        try:
            with open(word_list_file, "r") as file:
                self.words = {w.strip().lower() for w in file.readlines()}
        except FileNotFoundError:
            print("Error: words.txt file not found.")
            self.words = set()

    def is_valid_word(self, word: str) -> bool:
        """
        Check if a word exists in the word list.
        """
        return word.lower() in self.words

    def is_anagram(self, word1: str, word2: str) -> bool:
        """
        Return True if word1 and word2 are anagrams of each other.
        """
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word: str):
        """
        Find all anagrams of the given word inside the word list.
        """
        word = word.lower()
        return [
            w for w in self.words
            if w != word and self.is_anagram(word, w)
        ]
