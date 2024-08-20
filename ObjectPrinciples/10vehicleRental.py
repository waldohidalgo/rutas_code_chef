class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental_cost(self, days):
        # Default calculation based on rental rate
        return days * self.rental_rate


class Car(Vehicle):
    def __init__(self, model, rental_rate, seats):
        super().__init__(model, rental_rate)
        self.seats = seats

    def calculate_rental_cost(self, days):
        # Override the method to calculate cost based on seats, days, and rental rate
        return self.seats * days * self.rental_rate


# Write your code here
# Read input
s=input()
a,b,c=list(map(int,input().split()))
obj=Car(s,a,b)
print(obj.calculate_rental_cost(c))



# Create a Car object


# Calculate and display the rental cost


