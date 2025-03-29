from collections import deque
from typing import Deque


def first_move(queue: Deque[int]):
    if queue and len(queue)>1:
        removed_elem=queue.popleft()
        queue.append(removed_elem)

def second_move(queue: Deque[int]):
    if queue:
        queue.popleft()  

def aman(queue: Deque[int]):
    # 1 once and 2 once
    first_move(queue)
    second_move(queue)


def aks(queue: Deque[int]):
    # 1 twice and 2 once

    first_move(queue)
    first_move(queue)
    second_move(queue)


t=int(input())

for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    q=deque(arr)
    # aman first 1 , aks 0
    i=0
    while q:
        if i%2==0:
            aman(q)
        else:
            aks(q)

        if len(q)==1:
            print((i+1)%2,q[0])
            break              
        i+=1

    
    