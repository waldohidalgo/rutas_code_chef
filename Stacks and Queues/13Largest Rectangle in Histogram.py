def get_largest_area(arr):
    n=len(arr)
    rli=[n]*n
    stack=[]

    for i in range(n-1,-1,-1):
        while stack and arr[i]<=arr[stack[-1]]:
            stack.pop()
        if stack:
            rli[i]=stack[-1]

        stack.append(i)

    stack.clear()

    lli=[-1]*n
    for i in range(n):
        while stack and arr[i]<=arr[stack[-1]]:
            stack.pop()
        if stack:
            lli[i]=stack[-1]

        stack.append(i)

    max_area=float("-inf")
    for i in range(n):
        max_area=max(max_area,(rli[i]-lli[i]-1)*arr[i])
    return max_area

print(get_largest_area([5,5]))