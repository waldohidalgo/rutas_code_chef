from typing import TypeVar

T = TypeVar('T')  # Declare a type variable 'T'

class Box:
    def __init__(self, item: T):
        self.item = item
    
    def get_item(self) -> T:
        return self.item

# Usage
string_box = Box("Hello")
print(string_box.get_item())  # Output: Hello

integer_box = Box(42)
print(integer_box.get_item())  # Output: 42