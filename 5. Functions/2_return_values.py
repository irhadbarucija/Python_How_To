# The value the function returns is called a return value. The return statement takes a value
# from inside a function and sends it back to the line that called the function.


# Returning a Simple Value
def favorite_pet_food(pet_name, pet_food): # Parameters
    """Return a full sentence, neatly formatted."""
    full_sentence = f"{pet_name}, needs to eat {pet_food} food."
    return full_sentence.title()

pet = favorite_pet_food('mona', 'monoprotein') # Arguments
print(pet)


# Making an Argument Optional

# Sometimes it makes sense to make an argument optional, so that people using the function can 
# choose to provide extra information only if they want to. You can use default values to make
# an argument optional.
def favorite_pet_food(pet_name, pet_food, pet_middle_name=''):
    """Return a full sentence, neatly formatted."""
    if pet_middle_name:
        full_sentence = f"{pet_name.title()}, also known as {pet_middle_name.title()}, and she likes to eat {pet_food.title()} food."
    else:
        full_sentence = f"{pet_name.title()}, she likes to eat {pet_food.title()} food."
    return full_sentence

pet = favorite_pet_food('mona', 'garbage')
print(pet)


# Returning a Dictionary

# A function can return any kind of value you need it to, including more complicated data structures
# like lists and dictionaries.
def build_car(car_engine, car_model, power=None):
    """Return a dictionary of information about a person."""
    car = {'engine': car_engine, 'model': car_model}
    if power:
        car['power'] = power
    return car

buyer = build_car('petrol', 'supra', power=115)
print(buyer)


# Using a Function with a while Loop
def build_car(car_engine, car_model):
    car = f"{car_engine} {car_model}"
    return car.title()

while True:
    print("\nPlease choose your car specifications: ")
    print("(enter 'q' at any time to quit)")

    engine = input("Car engine: ")
    if engine == 'q':
        break

    model = input("Car model: ")
    if model == 'q':
        break

    full_car = build_car(engine, model)
    print(f"\nYour car is {full_car}!")