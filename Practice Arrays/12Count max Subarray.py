def countSubarrays(arr, n, k):
    # Write your code here
        n=len(arr)
        left=[0]*n
    
        stack=[]
        for i in range(n):
            while stack and arr[stack[-1]]<k:
                stack.pop()
            left[i]=stack[-1] if stack else -1
            stack.append(i)


        stack.clear()
        right=[0]*n
        # aca considero los iguales pero arriba no ya que ya fueron considerados
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]<=k:
                stack.pop()
            right[i]=stack[-1] if stack else n
            stack.append(i)



        count=0
        for i in range(n):
            if arr[i]==k:
                count+=(i-left[i])*(right[i]-i)
        return count        

if __name__ == "__main__":
    #N, K = list(map(int, input().split()))
    #arr =[2,1,3,4,5,3,2] #list(map(int, input().split()))
    arr=[1,2,1]
    print(countSubarrays(arr, len(arr), 1))