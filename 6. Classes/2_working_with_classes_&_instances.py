# Once you write a class, you'll spend most of your time working with instances created from that class.
# One of the first tasks you'll want to do is modify the attributes associated with a particular instance.
# You can modify the attributes of an instance directly or write methods that update attributes in specific ways.

class UsedCarShop:

    # We define the __init__() method with the self parameter first, then we give it three other parameters. The
    # __init__() method takes in these parameters and assigns them to the attributes that will be associated with
    # instances made from this class.
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # When an instance is created , attributes can be defined without being passed in as parameters.
        self.odometer_reading = 0

    # We define a method called car_description() that put's a car's year, make, and model into one string. This will
    # spares us from having to print each attribute's value individually. To work with the attribute values in this 
    # method, we use self.make, self.model, and self.year.
    def car_description(self):
        full_description = f"{self.year} {self.make} {self.model}"
        return full_description.title()
    
    def odometer_status(self):
        print(f"This car has {self.odometer_reading} kilometers on it.")
    
    # Instead of accessing the attribute directly, you pass the new value to a method that handles the updating internally.
    # We also can add a little logic to make sure no one tries to roll back the odometer:
    def update_odometer(self, kilometers):
        if kilometers >= self.odometer_reading:
            self.odometer_reading = kilometers
        else:
            print("You can't roll back an odometer!")

    # Sometimes you'll want to increment an attribute's value by a certain amount, rather than set an entirely new value:
    def increment_odometer(self, kilometers):
        self.odometer_reading += kilometers

# Outside of the class, we make an instance from the UsedCarShop class and assign it to the variable my_new_car. Then we
# call car_description() to show what kind of car we have.
my_new_car = UsedCarShop('peugeot', '207', 2009)
print(my_new_car.car_description())

# The simplest way to modify the value of an attribute is to access the attribute directly through an instance:
my_new_car.odometer_reading = 123_000
my_new_car.update_odometer(121_000)
my_new_car.increment_odometer(329)
my_new_car.odometer_status()
