t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    # your code goes here
    arr.sort(reverse=True)
    stones=0
    for i in range(0,n,2):
        stones+=arr[i]
    print(stones)