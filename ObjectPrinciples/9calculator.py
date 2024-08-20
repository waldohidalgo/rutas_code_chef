class Calculator:

    # Method to add integers
    def add(self, *args):
        sum = 0

        for num in args:
            sum += num

        return sum

    def multiply(self,*args):
        if len(args)==0:
            return
        if len(args)==1:
            return args[0]
        else:
            mul=args[0]
            for i in args[1:]:
                mul*=i
            return mul




calculator = Calculator()

# Using the different overloaded add methods
mul1=calculator.multiply(2,3,4,5)
print(mul1)