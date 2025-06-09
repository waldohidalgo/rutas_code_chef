t=int(input())
for _ in range(t):
    n=int(input())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    arr1.sort(reverse=True)
    arr2.sort()
    print(arr1)
    print(arr2)