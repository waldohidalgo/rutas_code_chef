#!/c/Python312/python
from math import gcd
# cook your dish here
t=int(input())
for case in range(t):
    n=int(input())
    arr=list(map(int,input().split()))

    if n==1:
        print(1)
    else:    
        prefixGCD=[1]*n
        suffixGCD=[1]*n
        sumTotal=0
        for i in range(n):
            if i==0:
                prefixGCD[i]=arr[i]
                suffixGCD[n-1-i]=arr[n-1-i]
            else:
                prefixGCD[i]=gcd(prefixGCD[i-1],arr[i])
                suffixGCD[n-1-i]=gcd(suffixGCD[n-1-i+1],arr[n-1-i])

            sumTotal+=arr[i]

        minCount=float('inf')
        for i in range(n):
            if i==0:
                restGCD=suffixGCD[i+1]
            elif i==n-1:
                restGCD=prefixGCD[i-1]
            else:
                restGCD=gcd(suffixGCD[i+1],prefixGCD[i-1])
            count=1+(sumTotal-arr[i])//restGCD
            minCount=min(minCount,count)

        print(minCount)