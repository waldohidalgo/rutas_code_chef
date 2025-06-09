import heapq
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    # your code goes here
    print(heapq.nlargest(x,a)[-1]-1)
