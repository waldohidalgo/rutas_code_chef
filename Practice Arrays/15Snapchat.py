t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t -= 1
    # Your code goes here
    max_streak=0
    count=0
    for i in range(n):
        if a[i]>0 and b[i]>0:
            count+=1
            max_streak=max(max_streak,count)
        else:
            count=0
    print("count",max_streak)