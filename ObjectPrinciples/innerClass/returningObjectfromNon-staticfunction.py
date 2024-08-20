class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        result_real = self.real + other.real
        result_imaginary = self.imaginary + other.imaginary
        return Complex(result_real, result_imaginary)


num1 = Complex(2.5, 3.0)
num2 = Complex(1.0, -1.5)

result = num1.add(num2)

print("Result: {} + {}i".format(result.real, result.imaginary))
