from collections import deque
from typing import Deque
def alice(s:Deque[str],t:Deque[str]):
    chr=s.popleft()
    if t and chr=="0":
        t.appendleft(chr)
    else:
        t.append(chr)

def bob(s:Deque[str],t:Deque[str]):
    chr=s.pop()
    if t and chr=="1":
        t.appendleft(chr)
    else:
        t.append(chr)

for _ in range(int(input())):
    n=int(input())
    s=input()
    q=deque(s)
    t=deque()
    i=0
    while q:
        if i%2==0:
            alice(q,t)
        else:
            bob(q,t)
        i+=1

    print("".join(t))