#!/c/Python312/python
# cook your dish here


def getMSBit(num):
    return num.bit_length()


t=int(input())

for case in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    prefix=[[0]*31 for _ in range(n+1)]
    for i in range(n):
        msbElement=getMSBit(arr[i])
        for j in range(31):
            if j==msbElement:
                prefix[i+1][j]=prefix[i][j]+1
            else:
                prefix[i+1][j]=prefix[i][j]

    q=int(input())

    for _ in range(q):
        l,r,x=map(int,input().split())
        b=getMSBit(x)
        print(r-l+1-(prefix[r][b]-prefix[l-1][b]))

    
            