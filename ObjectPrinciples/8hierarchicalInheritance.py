# Base class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print("Starting the", self.make, self.model)

    def stop(self):
        print("Stopping the", self.make, self.model)

# Derived class Car inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, numberOfDoors):
        super().__init__(make, model)
        self.numberOfDoors = numberOfDoors

    def honk(self):
        print("Honking the horn of the", self.make, self.model)

# Derived class Motorcycle inheriting from Vehicle
class Motorcycle(Vehicle):
    def __init__(self, make, model, engineType):
        super().__init__(make, model)
        self.engineType = engineType

    def wheelie(self):
        print("Performing a wheelie on the", self.make, self.model)

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 4)
my_car.start()
my_car.honk()
my_car.stop()

# Create an instance of the Motorcycle class
my_motorcycle = Motorcycle("Harley-Davidson", "Sportster", "4-stroke")
my_motorcycle.start()
my_motorcycle.wheelie()
my_motorcycle.stop()

