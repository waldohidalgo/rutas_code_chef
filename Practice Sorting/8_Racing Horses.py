t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    # your code goes here
    s.sort()
    min_diff=s[-1]-s[0]
    for i in range(1,n-1):
        if s[i]-s[i-1]<min_diff:
            min_diff=s[i]-s[i-1]
    print(min_diff)