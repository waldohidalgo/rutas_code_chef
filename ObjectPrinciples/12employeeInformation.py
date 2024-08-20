class Employee:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print("Name:", self.name)


class Worker(Employee):
    def __init__(self, name, hourly_rate):
        super().__init__(name)
        self.hourly_rate = hourly_rate

    def display_info(self):
        super().display_info()  # Call the base class method
        print("Hourly Rate: $" + str(self.hourly_rate))


# take input
name=input()
rate=int(input())

# Create object of Worker class
worker=Worker(name,rate)


# Use dynamic method dispatch to display worker information
worker.display_info()


