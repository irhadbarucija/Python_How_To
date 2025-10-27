# DICTIONARIES
# A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use
# a key to access the value associated with that key. You can use any object that you create in Python as a 
# value in a dictionary.
car_0 = {'color': 'green', 'engine': 'petrol'}

print(car_0['color'])
print(car_0['engine'])


# ACCESSING VALUES IN A DICTIONARY
# To get the value associated with a key, give the name of the dictionary and then place the key inside a set
# of square brackets:
car_0 = {'color': 'yellow', 'engine': 'diesel'}

car_engine = car_0['engine']
print(f"Your car runs on {car_engine}.")


# ADDING NEW KEY-VALUE PAIRS
# Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time.
car_0 = {'color': 'green', 'engine': 'petrol'}
print(car_0)

car_0['horsepower'] = 115
car_0['price'] = 23_000
print(car_0)
# Dictionaries retain the order in which they were defined. When you print a dictionary or loop through its 
# elements, you will see the elements in the same order they were added to the dictionary.


# STARTING WITH AN EMPTY DICTIONARY
# It's sometimes convenient, or even necessary, to start with an empty dictionary and then add each new item to it.
# Typically, you'll use empty dictionaries when storing user-supplied data in a dictionary or when writing code that
# generates a large number of key-value pairs automatically.
car_0 = {}

car_0['color'] = 'yellow'
car_0['engine'] = 'diesel'

print(car_0)


# MODIFYING VALUES IN A DICTIONARY
car_0 = {'current speed': 120, 'top speed': 220, 'speed': 'medium'}
print(f"Current speed: {car_0['current speed']}.")

if car_0['current speed'] >= 180:
    add_throttle = 20
elif car_0['current speed'] >= 130:
    add_throttle = 40
else:
    add_throttle = 70

car_0['current speed'] = car_0['current speed'] + add_throttle

print(f"New current speed is {car_0['current speed']}.")


# REMOVING KEY-VALUE PAIRS
# When you no longer need a piece of information that's stored in a dictionary, you can use the del statement to 
# completely remove a key-value pair.
car_0 = {'color': 'blue', 'engine': 'diesel'}
print(car_0)

del car_0['engine']
print(car_0)

# NOTE: Be aware that the deleted key-value pair is removed permanently.


# A DICTIONARY OF SIMILAR OBJECTS
# You can also use dictionary to store one kind of information about many objects.
favorite_cities = {
    'mike': 'london',
    'jess': 'tokyo',
    'ivan': 'paris',
    'phil': 'berlin',
}

city = favorite_cities['ivan'].title()
print(f"Ivan's favorite city is {city}.")


# USING get() TO ACCESS VALUE
# For dictionaries specifically, you can use the get() method to set a default value that will be returned if the 
# requested key doesn't exists.
country = {'population': 3_000_000, 'language': 'english'}

visa_value = country.get('visa', 'No visa value assigned.')
print(visa_value)

# NOTE: If you leave out the second argument in the call to get() and the key doesn't exist, Python will return 
#       the value None. The special value None means "no value exists." This is not an error: it's a special value
#       meant to indicate the absence of a value.


# LOOPING THROUGH A DICTIONARY
# Because a dictionary can contain large amounts of data, Python lets you loop through a dictionary. You can loop
# through all of a dictionary's key-value pairs, through its keys, or through its values.


# LOOPING THROUGH ALL KEY-VALUE PAIRS
# To write a for loop for a dictionary, you create names for the two variables that will hold the key and value in 
# each key-value pair. You can choose any names you want for these two variables. The second half of the for statement
# includes the name of the dictionary followed by the method items(), which returns a sequence of key-value pairs.
# The for loop then assigns each of these pairs to the two variables provided.
favorite_language = {
    'eric': 'swift',
    'monica': 'python',
    'elsa': 'javascript',
    'paul': 'c++',
}

for name, language in favorite_language.items():
    print(f"\n{name.title()}'s favorite language is {language.title()}.")


# LOOPING THROUGH ALL THE KEYS IN A DICTIONARY
# The keys() method is useful when you don't need to work with all of the values in a dictionary.
favorite_language = {
    'eric': 'swift',
    'monica': 'python',
    'paul': 'c++',
    'elsa': 'javascript',
}

for name in favorite_language.keys():
    print(name.title())
# You can choose to use the keys() method explicitly if it makes your code easier to read, or you can omit it if 
# you wish.

# You can access the value associated with any key you care about inside the loop, by using the current key.
favorite_language = {
    'eric': 'swift',
    'monica': 'python',
    'paul': 'c++',
    'elsa': 'javascript',
}

friends = ['monica', 'paul']
for name in favorite_language.keys():
    print(f"\nHi {name.title()}")

    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()}'s favorite language is {language}!")

if 'jason' not in favorite_language.keys():
    print("\nJason, please.")


# LOOPING THROUGH A DICTIONARY'S KEYS IN A PARTICULAR ORDER
# Looping through a dictionary returns the items in the same order they were inserted. You can use the sorted() 
# function to get a copy of the keys in order:
favorite_cars = {
    'phil': 'bmw',
    'joseph': 'skoda',
    'erica': 'volkswagen',
    'adam': 'toyota',
}

for name in sorted(favorite_cars.keys()):
    print(f"{name.title()}, excellent choice.")


# LOOPING THROUGH ALL VALUES IN A DICTIONARY
# You can use the values() method to return a sequence of values without any keys. To see each value chosen without
# repetition, we can use a set. A set is a collection in which each item must be unique.
favorite_cars = {
    'phil': 'bmw',
    'joseph': 'skoda',
    'erica': 'volkswagen',
    'adam': 'toyota',
    'nick': 'skoda',
}

print("The following cars have been mentioned:")
for name in set(favorite_cars.values()):
    print(name.title())

# NOTE: You can build a set directly using braces and separating the elements with commas:
#       cars = {'audi', 'bmw', 'skoda'}. It's easy to mistake sets for dictionaries because they're 
#       both wrapped in braces. When you see braces but no key-value pairs, you're probably looking
#       at a set. Unlike lists and dictionaries, sets do not retain items in any specific order.


# NESTING
# Sometimes you'll want to store multiple dictionaries in a list, or a list of items as a value in a dictionary. 
# This is called nesting.


# A LIST OF DICTIONARIES
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)
print("...")

print(f"Total number of aliens: {len(aliens)}")


# A LIST IN A DICTIONARY
pizza = {
    'crust': 'thick',
    'toppings': ['pepperoni', 'mushrooms', 'cheese'],
}

print(f"You ordered a {pizza['crust']}--crust pizza with the: ")
for topping in pizza['toppings']:
    print(f"\t{topping}")

# NOTE: You should not nest lists and dictionaries too deeply. If you're nesting items much deeper than
#       what you see in the preceding examples, or if you're working with someone else's code with significant
#       levels of nesting, there's most likely a simpler way to solve the problem.


# A DICTIONARY IN A DICTIONARY
users = {
    'sman': {
        'first': 'spider',
        'last': 'man',
        'work': 'photographer',
    },
    'bman': {
        'first': 'bat',
        'last': 'man',
        'work': 'ceo',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    work = user_info['work']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tWork: {work.title()}")