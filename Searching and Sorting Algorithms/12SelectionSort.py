n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    m_i=i
    for j in range(i+1,n):
        if arr[j]<arr[m_i]:
            m_i=j
    arr[m_i],arr[i]=arr[i],arr[m_i]

print(*arr)
