# cook your dish here
t=int(input())
for _ in range(t):
    s=input()
    i=0
    ct=0
    while i<len(s)-1:
        if s[i]==s[i+1]:
            i+=1
        else:
            ct+=1
            i+=2
    print(ct)