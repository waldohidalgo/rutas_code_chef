from typing import TypeVar

T = TypeVar('T')

# A generic method to find the maximum element in an array.
def find_max(arr: list[T]) -> T:
    # Write your code here
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            arr[i+1],arr[i]=arr[i],arr[i+1]
    return arr[-1]


# Example arrays
int_array = [5, 12, 3, 8, 9]
double_array = [2.4, 6.7, 1.8, 9.2, 4.5]

# Calculate the maximum elements using the generic method and print the results
print(find_max(int_array))
print(find_max(double_array))
