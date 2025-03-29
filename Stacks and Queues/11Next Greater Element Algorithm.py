def next_greater_element(arr):
    n=len(arr)
    res=[-1]*n
    stack=[]
    for i in range(n-1,-1,-1):
        while stack and arr[i]>=stack[-1]:
            stack.pop()
        curr_elem=arr[i]
        arr[i]=stack[-1] if stack else -1

        stack.append(curr_elem)

    return arr

arr= [4,5,3,2,1]

next_greater_element(arr)
print(arr)