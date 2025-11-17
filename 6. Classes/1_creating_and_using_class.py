# OOP -- Object-oriented programming is one of the most effective approaches to writing software. In object-oriented
# programming, you write classes that represents real-world things and situations, and you create objects based on 
# these classes.

# CREATING AND USING A CLASS
# 1. Making an object from a class is called instantiation, and you work with instances of a class.
# 2. A function that's part of a class is a method.
# 3. The __init__() method is a special method. A convention that helps prevent Python's default method names. We define
#    the __init__() method in our example with three parameters: self, name, and age. The self parameter is required in
#    the method definition, and it must come first, before the other parameters. When Python calls this method later, the 
#    method call will automatically pass the self argument. It gives the individual instance access to the attributes and 
#    methods in the class.
# 4. The two variables defined in the body of the __init__() method each have the prefix self. Any variable prefixed with
#    self is available to every method in the class, and we'll also be able to access these variables through any instance
#    created from the class. Variables that are accessible through instances like this are called attributes.
class Cat:
    """A simple attempt to model a cat."""

    # special method
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name # takes value associated with the parameter name and assigns it to the variable name
        self.age = age

    # method
    def purr(self):
        """Simulate a cat purring."""
        print(f"{self.name} is now purring.")

    def sleep(self):
        """Simulate a cat sleeping."""
        print(f"{self.name} is sleeping now.")

# Making an instance from a class
# Here, we tell Python to create a cat whose name is "Simba" and whose age is 3. When Python reads this line, it calls
# the __init__() method in Cat with the arguments 'Simba' and 3. The __init__() method creates an instance representing
# this particular cat and sets the name and age attributes using the values we provided. Python then returns an instance
# representing this cat. We assign that instance to the variable my_cat.
my_cat = Cat('Simba', 3) 

# Accessing Attributes
# To access the attributes of an instance, you use dot notation: my_cat.name Here Python looks at the instance my_cat and then 
# finds the attribute name associated with my_cat. This is the same attribute referred to as self.name in the class Cat.
print(f"My cat's name is {my_cat.name}.")
print(f"My cat is {my_cat.age} years old.")

# Calling Methods
# After we create an instance from the class Cat, we can use dot notation to call any method defined in Cat. When Python reads
# my_cat.purr(), it looks for the method purr() in the class Cat and runs that code.
my_cat.purr()
my_cat.sleep()

# Creating Multiple Instances
your_cat = Cat('Harry', 5)

print(f"\nYour cat's name is {your_cat.name} and it's {your_cat.age} years old.")

your_cat.sleep()
your_cat.purr()