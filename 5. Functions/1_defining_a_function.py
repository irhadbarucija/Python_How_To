# This is the function definition, which tells Python the name of the function
# and, if applicable, what kind of information the function needs to do its job.
# The parentheses hold that information, in this case it's empty.
def car_parts():
    """Display car part."""
    print("Bushings!")

car_parts()


# PASSING INFORMATION TO A FUNCTION
def car_parts(tire_size, season):
    """Display car tires information."""
    print(f"Tire size is {tire_size} and it's for {season}.")

car_parts(17, 'summer')


# ARGUMENTS AND PARAMETERS
# In the example above, the variable tire_size and season in the definition of 
# car_parts is an example of parameter, a piece of information the function needs
# to do its job. The value 17 and 'summer' in car_parts(17, 'summer') is an example
# of an argument. An argument is a piece of information that's passed from a 
# function call to a function. When we call the function, we place the value we want 
# the function to work with in parentheses.