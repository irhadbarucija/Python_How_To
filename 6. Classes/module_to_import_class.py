"""A class that can be used to represent a car."""
class UsedCarShop:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def car_description(self):
        full_description = f"{self.year} {self.make} {self.model}"
        return full_description.title()
    
    def odometer_status(self):
        print(f"This car has {self.odometer_reading} kilometers on it.")

    def update_odometer(self, kilometers):
        if kilometers >= self.odometer_reading:
            self.odometer_reading = kilometers
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, kilometers):
        self.odometer_reading += kilometers