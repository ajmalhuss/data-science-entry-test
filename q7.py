class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """
    def __init__(self, make, model, year): #to automatically assign the variables
        self.make = make #assigns make to the given value mak
        self.model = model #assigns model to the given value model
        self.year = year #assigns year to the given value year

    def describe_car(self): #method to print the car
        print(f"{self.make} {self.year} {self.model}") #prints using the value assigned above


# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020
car = Car("Toyota", "Corolla", 2020)
car.describe_car()
