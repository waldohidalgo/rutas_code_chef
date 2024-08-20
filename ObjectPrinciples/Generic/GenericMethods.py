from typing import TypeVar, List

T = TypeVar('T')  # Declare type variable

def process_items(items: List[T]) -> List[T]:
    processed_items = []  # Initialize an empty list for processed items
    for item in items:
        # Process each item here
        processed_item = item * 2  # Example processing, just doubling the value
        processed_items.append(processed_item)
    return processed_items

# Usage
integer_list = [1, 2, 3, 4, 5]
processed_integer_list = process_items(integer_list)
print(processed_integer_list)  # Output: [2, 4, 6, 8, 10]

string_list = ['a', 'b', 'c']
processed_string_list = process_items(string_list)
print(processed_string_list)  # Output: ['aa', 'bb', 'cc']