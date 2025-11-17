# ============================================
# DAILY CHALLENGE - OOP QUIZZ
# ============================================
# This file contains:
# - Theoretical answers (Quiz)
# - Practical implementation of a Deck of Cards
# ============================================


# ============================
# EXERCISE 1: OOP QUIZZ
# ============================

"""
1) What is a class?
   → A class is a blueprint or template that defines the attributes and behaviors (methods)
     of the objects created from it.

2) What is an instance?
   → An instance is a concrete object created from a class.
     Example: if 'Car' is a class, then 'my_car = Car()' is an instance.

3) What is encapsulation?
   → Encapsulation is the concept of bundling data (attributes) and methods that operate
     on that data into a single unit (class). It also helps protect data by making attributes private.

4) What is abstraction?
   → Abstraction means hiding complex details and showing only the essential features of an object.

5) What is inheritance?
   → Inheritance allows a class to inherit attributes and methods from another class.
     Example: 'Dog' can inherit from 'Animal'.

6) What is multiple inheritance?
   → Multiple inheritance occurs when a class inherits from more than one parent class.

7) What is polymorphism?
   → Polymorphism allows the same method to behave differently depending on the object that calls it.
     Example: 'animal.speak()' might print "Woof" for a Dog and "Meow" for a Cat.

8) What is MRO (Method Resolution Order)?
   → MRO defines the order in which Python looks for a method in a hierarchy of classes,
     especially when multiple inheritance is used.
"""


# ============================
# EXERCISE 2: DECK OF CARDS
# ============================

import random

# -----------------------------
# Class representing a single card
# -----------------------------
class Card:
    def __init__(self, suit, value):
        self.suit = suit      # Hearts, Diamonds, Clubs, Spades
        self.value = value    # A, 2, 3, ..., 10, J, Q, K

    def __repr__(self):
        """Return a readable representation of the card"""
        return f"{self.value} of {self.suit}"


# -----------------------------
# Class representing a full deck of 52 cards
# -----------------------------
class Deck:
    def __init__(self):
        """Initialize the deck with 52 cards"""
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
