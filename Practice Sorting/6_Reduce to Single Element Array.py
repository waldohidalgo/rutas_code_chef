def main():
    # Write your code here
    n=int(input())
    arr=list(map(int,input().split()))
    # your code goes here
    arr.sort()
    if n==1:
        print("YES")
    else:
        for i in range(1,n):
            if arr[i]-arr[i-1]>1:
                print("NO")
                break
        else:
            print("YES")

if __name__ == "__main__":
    main()