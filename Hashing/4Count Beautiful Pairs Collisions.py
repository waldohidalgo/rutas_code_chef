M = 999983
MX = 1000000000

hash =  [[] for _ in range(M)]

# Hash Function
def f(x):
    return x % M

# Write your code here
def beautiful_pairs(arr):
    n = len(arr)
    ct = 0

    for i in range(n):
        hashed_value = f(arr[i] * arr[i])
        
        ct += sum(1 for val in hash[hashed_value] if val == arr[i] * arr[i])
        
        hash[f(arr[i])].append(arr[i])

    return ct


arr=[4,999983+4,2,2]
print(beautiful_pairs(arr))


