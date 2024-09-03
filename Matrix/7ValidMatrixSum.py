#!/c/Python312/python

def main():
    # Write your code here
    n,m=map(int,input().split())
    if (n*m)%2==0:
        for i in range(n):
            for j in range(m):
                print(1,end=" ")
            print()
    else:
        return -1

if __name__ == "__main__":
    main()