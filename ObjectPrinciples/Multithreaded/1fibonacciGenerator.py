def fibonacci_generator():
    # Initialize variables for the first two Fibonacci numbers
    a, b = 0, 1
    
    # Infinite loop to generate Fibonacci numbers
    while True:
        yield a  # Yield the current Fibonacci number
        a, b = b, a + b  # Update variables for the next Fibonacci number


n = int(input())
# Using the Fibonacci generator
fib_gen = fibonacci_generator()
for _ in range(n):
    print(next(fib_gen))
