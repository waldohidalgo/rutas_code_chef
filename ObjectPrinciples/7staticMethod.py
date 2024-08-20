class MathUtils:
    @staticmethod
    def square(num):
        return num * num

    @staticmethod
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * MathUtils.factorial(n - 1)


# Call the static methods directly using the class name
squared_value = MathUtils.square(5)
print("Square of 5 is:", squared_value)

factorial_value = MathUtils.factorial(5)
print("Factorial of 5 is:", factorial_value)


