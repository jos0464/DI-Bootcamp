class Animal:
    def __init__(self, name, count=1):
        self.name = name                # __init__
        self.count = count

    def __str__(self):
        return f"{self.name} : {self.count}"   # affichage lisible

    def __repr__(self):
        return f"Animal({self.name!r}, {self.count})"  # debug

    def __add__(self, other):
        if isinstance(other, Animal) and other.name == self.name:
            return Animal(self.name, self.count + other.count)  # addition
        raise ValueError("Cannot add different animals")

    def __eq__(self, other):
        return self.name == other.name and self.count == other.count  # égalité

    def __lt__(self, other):
        return self.count < other.count   # comparaison <

    def __len__(self):
        return self.count                 # len(obj) = nombre d'animaux

    def __call__(self):
        print(f"{self.name} says: Hello!")  # permet d'appeler l'objet comme une fonction

    def __getitem__(self, index):
        return f"{self.name}-{index}"      # accès type obj[index]

    def __setitem__(self, index, value):
        print(f"Setting {self.name}-{index} to {value}")

    def __enter__(self):
        print(f"Entering context for {self.name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Exiting context for {self.name}")

    def __del__(self):
        print(f"{self.name} is being deleted")

# --- TEST ---
cat1 = Animal("Cat", 3)
cat2 = Animal("Cat", 2)

print(cat1)               # __str__
print(repr(cat1))         # __repr__

cat3 = cat1 + cat2        # __add__
print(cat3)

print(cat1 == cat2)       # __eq__
print(cat1 < cat2)        # __lt__
print(len(cat1))          # __len__

cat1()                    # __call__
print(cat1[5])            # __getitem__
cat1[5] = "new"           # __setitem__

with cat1 as c:           # __enter__ / __exit__
    print("Inside context")

del cat1                  # __del__
