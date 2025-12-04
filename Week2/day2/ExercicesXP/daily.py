import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_idx = 0  # page index interne (0-based)
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    # Récupère les items visibles sur la page actuelle
    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    # Navigation vers une page spécifique (1-based)
    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"Page number {page_num} out of range (1-{self.total_pages})")
        self.current_idx = page_num - 1
        return self  # pour method chaining

    # Première page
    def first_page(self):
        self.current_idx = 0
        return self

    # Dernière page
    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    # Page suivante
    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    # Page précédente
    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    # Affichage des items visibles (bonus)
    def __str__(self):
        return "\n".join(str(item) for item in self.get_visible_items())

# ------------------------
# Tests
# ------------------------
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())  
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())  
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())  
# ['y', 'z']

try:
    p.go_to_page(10)
except ValueError as e:
    print(e)  
# Page number 10 out of range (1-7)

try:
    p.go_to_page(0)
except ValueError as e:
    print(e)  
# Page number 0 out of range (1-7)

# Exemple de method chaining
items_on_page = p.first_page().next_page().next_page().get_visible_items()
print(items_on_page)  
# ['i', 'j', 'k', 'l']

# Test de l'affichage avec __str__()
print(str(p))
# Affiche les items de la page actuelle, chaque élément sur une nouvelle ligne
