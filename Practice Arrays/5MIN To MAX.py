t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    # Your code goes here
    t -= 1
    minimum=min(a)
    count=0
    for el in a:
        if el!=minimum:
            count+=1
    print("count",count)