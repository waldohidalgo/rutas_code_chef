#!/c/Python312/python
# cook your dish here
t=int(input())
for testcase in range(t):
    n=int(input())
    ranges=[]
    for line in range(n):
        l,r=map(int,input().split())
        ranges.append((l,r))
    prefixIntersection=[(1,n)]+[None]*n
    suffixIntersection=[None]*n+[(1,n)]
    for i in range(n):
        l,r=ranges[i]
        if prefixIntersection[i]:
            lBefore,rBefore=prefixIntersection[i]
            if max(l,lBefore)<=min(r,rBefore):
                prefixIntersection[i+1]=(max(l,lBefore),min(r,rBefore))   
    for i in range(n-1,-1,-1):
        l,r=ranges[i]
        if suffixIntersection[i+1]:
            lBefore,rBefore=suffixIntersection[i+1]
            if max(l,lBefore)<=min(r,rBefore):
                suffixIntersection[i]=(max(l,lBefore),min(r,rBefore))
    count=0
    result=[]
    for i in range(1,n+1):
        l,r=ranges[i-1]
        if i<l or i>r:
            rangePrefix=prefixIntersection[i-1]
            rangeSuffix=suffixIntersection[i]
            if rangePrefix and rangeSuffix:
                if max(rangePrefix[0],rangeSuffix[0])<=i and i<=min(rangePrefix[1],rangeSuffix[1]):
                    count+=1
                    result.append(i)
    print(count)
    for i in result:
        print(i)

        
