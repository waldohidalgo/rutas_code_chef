# Function to calculate gcd of 2 integers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to calculate lcm of 2 integers
def lcm(a, b):
    return a * (b // gcd(a, b))

# Function to calculate lcm of 3 integers
def lcm_of_three(a, b, c):
    return lcm(a, lcm(b, c))

t = int(input())

for _ in range(t):
    n, a, b, c = map(int, input().split())
    # Write your code here
    cantidad_a = n // a
    cantidad_b= n // b
    cantidad_c= n // c
    cantidad_a_b=n//lcm(a,b)
    cantidad_a_c=n//lcm(a,c)
    cantidad_b_c=n//lcm(b,c)
    cantidad_a_b_c=n//lcm_of_three(a,b,c)
    cantidad_total=cantidad_a+cantidad_b+cantidad_c-cantidad_a_b-cantidad_a_c-cantidad_b_c+cantidad_a_b_c
    print(cantidad_total)