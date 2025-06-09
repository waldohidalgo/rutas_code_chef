t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # your code goes here
    a.sort()
    running_sum=0
    for i in range(k,n-k):
        running_sum+=a[i]
    print(running_sum/((n-2*k)))
