t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t -= 1
    # Your code goes here
    count=0
    for i in range(n):
        # alice is happy
        if b[i]<=2*a[i] and a[i]<=2*b[i]:
            count+=1
    print("count",count)
