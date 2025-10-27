# List allow you to store sets of information in one place, whether you
# have just a few items or millions of items. A list is a collection of
# items in a particular order. A list usually contains more than one element,
# it's a good idea to make the name of your list plural.

# Simple list example:
names = ['Josh', 'Ivy', 'Mona', 'Eric']
print(names)


# ACCESSING ELEMENTS IN A LIST
# Lists are ordered collections, you can access any element in a list by telling 
# the position, or index, of the item desired.
countries = ['Ireland', 'France', 'Australia']
print(countries[2])

# You can also use the string method on any element in a list:
print(countries[1].title())

# Python has a special syntax for accessing the last element in a list. This syntax
# is quite useful, because you'll often want to access the last item without knowing
# exactly how long the list is:
print(countries[-1])

# NOTE: Python considers the first item in a list to be at position 0, not
#       position 1.


# USING INDIVIDUAL VALUES FROM A LIST
# You can use f-strings to create a message based on a value from a list:
cities = ['New York', 'London', 'Tokyo', 'Sarajevo']
message = f"My favorite city is {cities[3].title()}, I like food there a lot!"
print(message)


# MODIFYING ELEMENTS IN A LIST
# You can change the value of any item in a list. The syntax is similar for accessing
# an element in a list:
colors = ['blue', 'red', 'black']
print(colors)

colors[1] = 'yellow'
print(colors)


# ADDING ELEMENTS TO A LIST
# The simplest way to add a new element to a list is to append the item to the list. 
# When you append an item to a list, the new element is added to the end of the list:
random_words = ['sky', 'frog', 'building']
print(random_words)

random_words.append('airplane')
print(random_words)

# The append() method makes it easy to build lists dynamically. You can start with an
# empty list and then add items to the list using a series of append() calls:
instruments = []

instruments.append('violin')
instruments.append('piano')
instruments.append('trumpet')

print(instruments)


# INSERTING ELEMENTS INTO A LIST
# You can add a new element at any position in your list by using the insert() method:
cars = ['bmw', 'mercedes', 'honda']
cars.insert(1, 'toyota')
cars.insert(0, 'audi')
print(cars)


# REMOVING AN ITEM USING THE del STATEMENT
# If you know the position of the item you want to remove from a list, you can use the
# del statement:
rivers = ['amazon', 'dunav', 'sava']
print(rivers)

del rivers[1]
print(rivers)
# You can remove an item from any position in a list using the del statement if you 
# know its index.


# REMOVING AN ITEM USING pop() METHOD
# Sometimes you'll want to use the value of an item after you remove it from a list. 
# The pop() method removes the last item in a list, but it lets you work with that 
# item after removing it.
motorcycles = ['yamaha', 'honda', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)


# POPPING ITEMS FROM ANY POSITION IN A LIST
# You can use pop() to remove an item from any position by including the index of 
# the item you want to remove:
phones = ['samsung', 'iphone', 'xiaomi', 'huawei']
first_owned = phones.pop(0)
print(f"The first phone I owned was a {first_owned.title()}.")

# NOTE: remember that each time you use pop(), the item you work with is no longer
#       stored in the list.

# If you're unsure whether to use del statement or the pop() method: when you want
# to delete an item from a list and not use that item in any way, use the del statement;
# if you want to use an item as you remove it, use the pop() method.


# REMOVING AN ITEM BY VALUE
# If you only know the value of the item you want to remove, you can use the remove() method.
shoes = ['puma', 'nike', 'adidas', 'converse']
print(shoes)

shoes.remove('puma')
print(shoes)

# You can also use the remove() method to work with a value that's being removed from a list:
too_expensive = 'nike'
shoes.remove(too_expensive)
print(shoes)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# NOTE: the remove() method deletes only the first occurrence of the value you specify. 
#       If there's a possibility the value appears more than once in the list, you'll 
#       need to use a loop to make sure all occurrences of the value are removed.


# SORTING A LIST PERMANENTLY WITH THE sort() METHOD
# The sort() method changes the order of the list permanently.
letters = ['c', 'h', 'a', 'z', 'd']
print(letters)
letters.sort()
print(letters)

# You can also pass the argument reverse=True to sort this list in reverse-alphabetical.
# Again, the order of the list is permanently changed:
letters.sort(reverse=True)
print(letters)


# SORTING A LIST TEMPORARILY WITH THE sorted() FUNCTION
# To maintain the original order of a list but present it in a sorted order we use the 
# sorted() function. It lets you display your list in a particular order, but doesn't affect
# the actual order of the list.
new_cars = ['ferrari', 'bugatti', 'alfa romeo']

print("Here is the original list:")
print(new_cars)

print("\nHere is the sorted list:")
print(sorted(new_cars))

print("\nHere is the original list again:")
print(new_cars)


# PRINTING A LIST IN REVERSE ORDER
# To reverse the original order of a list, you can use the reverse() method. It simply reverses
# the order of the list. It changes the order of a list permanently, but you can revert to the
# original order anytime by applying reverse() again:
superheroes = ['ironman', 'spiderman', 'aquaman', 'captain america']
print(superheroes)
superheroes.reverse()
print(superheroes)
superheroes.reverse()
print(superheroes)


# FINDING THE LENGTH OF A LIST
# You can quickly find the length of a list by using the len() function. You'll find len() useful
# when you to determine the amount of data you have to manage in a visualization, or figure out the
# number of registered users on a website, among other tasks.
print(len(superheroes))