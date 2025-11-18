import module_to_import_class
# Python lets you store classes in modules and then import the classes you need into your main program.


my_used_car = module_to_import_class.UsedCarShop('audi', 'rs3', 2023)
print(my_used_car.car_description())

my_used_car.odometer_reading = 4323
my_used_car.odometer_status()



# Inheritance
# When one class inherits from another, it takes on the attributes and methods of the first class. 
# The original class is called the parent class, and the new class is the child class. The child 
# class can inherit any or all of the attributes and methods of its parent class, but it's also free
# to define new attributes and methods of its own.

# When you're writing a new class based on an existing class, you'll often want to call the __init__()
# method from the parent class. This will initialize any attributes that were defined in the parent 
# __init__() method and make them available in the child class.
class ElectricCar(module_to_import_class.UsedCarShop):
    """Represents aspcets of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        # You can add any new attributes and methods necessary to differentiate the child class from 
        # the parent class.
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn't have a gas tank!")

# Instances as Attributes
# You can break your large class into smaller classes that work together; this approach is called composition.
class Battery:

    def __init__(self, battery_size=50):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}--kWh battery.")
        
    def get_range(self):
        if self.battery_size == 50:
            range = 200
        elif self.battery_size == 65:
            range = 225
        
        print(f"This car can go about {range} kilometers on a full charge.")


my_electric_car = ElectricCar('toyota', 'yaris', 2024)
print(my_electric_car.car_description())
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()