import math

class Circle:
    def __init__(self, radius):
        self._radius = radius

    # Property for radius
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    # Property for diameter (computed from radius)
    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        if value <= 0:
            raise ValueError("Diameter must be positive")
        self._radius = value / 2

    # Compute area
    def area(self):
        return math.pi * self._radius ** 2

    # String representation
    def __str__(self):
        return f"Circle with radius: {self._radius:.2f}"

    def __repr__(self):
        return f"Circle(radius={self._radius:.2f})"

    # Add two circles (new circle with sum of radii)
    def __add__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("Can only add Circle to Circle")
        return Circle(self._radius + other._radius)

    # Comparison operators
    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius > other._radius

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius == other._radius

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius < other._radius


# =========================
# Testing the Circle class
# =========================

c1 = Circle(5)
c2 = Circle(3)
c3 = Circle(7)

# Access radius and diameter
print(c1.radius)     # 5
print(c1.diameter)   # 10

# Set diameter (updates radius automatically)
c2.diameter = 8
print(c2.radius)     # 4.0
print(c2.diameter)   # 8.0

# Compute area
print(f"Area of c1: {c1.area():.2f}")  # 78.54

# String representation
print(c1)             # Circle with radius: 5.00
print(repr(c2))       # Circle(radius=4.00)

# Add two circles
c4 = c1 + c3
print(c4)             # Circle with radius: 12.00

# Comparisons
print(c1 > c2)        # True
print(c2 < c3)        # True
print(c1 == Circle(5))# True

# Sorting circles
circle_list = [c1, c2, c3, c4]
circle_list.sort()
print(circle_list)    # Sorted by radius
