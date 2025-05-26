n=int(input())
st=set()
for _ in range(n):
    a,b=map(int,input().split())
    st.add((a,b))
p,q=map(int,input().split())
if (p,q) in st or (q,p) in st:
    print("Yes")
else:
    print("No")