# cook your dish here
data=input().split()
s1=data[0]
c1=data[1]
k=int(data[2])

count=0
isFound=False
for i,ch in enumerate(s1):
    if ch==c1:
        count+=1
    if count==k:
        print(i)
        isFound=True
        break
if not isFound:
    print(-1)
