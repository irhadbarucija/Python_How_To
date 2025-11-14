# Because a function definition can have multiple parameters, a function call may need
# multiple arguments. You can pass arguments to your functions in a number of ways. 
# You can use positional arguments , which need to be in the same order the parameters
# were written; keyword arguments, where each argument consists of a variable name and a
# value; and lists and dictionaries of values.


# POSITIONAL ARGUMENTS
# When you call a function, Python must match each argument in the function call with a
# parameter in the function definition. Values matched up this way are called positional
# arguments. Order matters in positional arguments. Make sure the order of the arguments
# in your function call matches the order of parameters in the function's definition.

def describe_pet(animal_type, animal_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {animal_name.title()}.")

describe_pet('dog', 'mona')


# KEYWORD ARGUMENTS
# A keyword argument is a name-value pair that you pass to a function. Keyword arguments
# free you from having to worry about correctly ordering your arguments in the function call,
# and they clarify the role of each value in the function call.
def describe_pet(animal_type, animal_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {animal_name.title()}.")

describe_pet(animal_type='cat', animal_name='harry')

# NOTE: When you use keyword arguments, be sure to use the exact names of the parameters in
#       the function's definition.


# DEFAULT VALUES
# When writing a function, you can define a default value for each parameter. If an argument 
# for a parameter is provided in the function call, Python uses the argument value. If not, it
# uses the parameter's default value.
def describe_pet(animal_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {animal_name.title()}.")

describe_pet(animal_name='Sumsirka')
# Because an explicit argument for animal_type is provided, Python will ignore the parameter's
# default value:
describe_pet(animal_name='ron', animal_type='fish')

# NOTE: When you use the default values, any parameter with a default value needs to be listed
#       after all the parameters that don't have default values. This allows Python to continue
#       interpreting positional arguments correctly.

