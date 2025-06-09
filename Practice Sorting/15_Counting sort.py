def frequency_based_sort(n, arr):
    # Write your code here
    min_value = min(arr)
    max_value = max(arr)

    frequency = [0] * (max_value - min_value + 1)

    for num in arr:
        frequency[num - min_value] += 1

    sorted_arr = []
    for i in range(n):
        val=arr[i]
        sorted_arr.append((frequency[val - min_value], val))

    sorted_arr.sort()

    for pair in sorted_arr:
        print(pair[1], end=" ")

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    # Function call to perform frequency-based sorting
    frequency_based_sort(n, arr)