def rec(m,x,y,arr):
    res=[True]*101
    res[0]=False
    arr.sort()
    cover=x*y
    end=0  
    for i in arr:
        [curr_s,curr_e]=[i-cover if i-cover>=1 else 1,i+cover if i+cover<=100 else 100]
        start=max(curr_s,end)
        for i in range(start,curr_e+1):
            res[i]=False
        end=curr_e
    return sum(res)

# cook your dish here
t=int(input())
for _ in range(t):
    m,x,y=map(int,input().split())
    arr=list(map(int,input().split()))
    print(rec(m,x,y,arr))






        
    