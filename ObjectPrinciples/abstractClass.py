from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

# Example usage:
circle = Circle(radius=5)
square = Square(side_length=4)

print("Circle Area:", circle.area())          # Output: 78.5
print("Square Area:", square.area())            # Output: 16