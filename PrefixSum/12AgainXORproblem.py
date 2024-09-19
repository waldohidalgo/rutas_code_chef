#!/c/Python312/python
# cook your dish here
t=int(input())
for testcase in range(t):
    n,k=map(int,input().split())
    s=input()
    prefixXOR=[0]*(n+1)
    for i in range(n):
        prefixXOR[i+1]=prefixXOR[i]^int(s[i])

    count=0
    for i in range(k):
        count+=prefixXOR[i]^prefixXOR[i+n-k+1]

    print('val',count)
    
   