#!/c/Python312/python
# cook your dish here
from math import gcd as getMCD
n=int(input())
arr=list(map(int,input().split()))


prefixGCD=[0]*n
suffixGCD=[0]*n
for i in range(n):
    if i==0:
        prefixGCD[i]=arr[i]
        suffixGCD[n-1-i]=arr[n-1-i]
    else:
        prefixGCD[i]=getMCD(prefixGCD[i-1],arr[i])
        suffixGCD[n-1-i]=getMCD(suffixGCD[n-1-i+1],arr[n-1-i])

maxGCD=suffixGCD[0]

for i in range(1,n-1):
    mcd=getMCD(suffixGCD[i+1],prefixGCD[i-1])
    maxGCD=max(maxGCD,mcd)

maxGCD=max(maxGCD,prefixGCD[n-2])
print(maxGCD)




