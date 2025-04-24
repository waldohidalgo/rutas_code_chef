t = int(input())

while t > 0:
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # Your code goes here
    t -= 1
    cost=0
    for i in range(n):
        if a[i]>=x:
            cost+=b[i]
    print("cost",cost)