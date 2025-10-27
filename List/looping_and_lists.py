# Looping allows you to take the same action, or set of actions, with every item in a list.

# simple for loop example:
dogs = ['mona', 'rex', 'maori', 'nala']
for dog in dogs:
    print(dog.title())
# Line number 4 tells Python to pull a name from the list dogs, and associate it with the variable
# dog. Then, we tell Python to print the name that's just been assigned to dog. It might help to
# read this code as "For every dog in the list of dog_names, print the dog's name."


# Looping is important because it's one of the most common ways a computer automates repetitive tasks. 
# Keep in mind that the set of steps is repeated once for each item in the list, no matter how many
# items are in the list. It's helpful to choose a meaningful name that represents a single item from 
# the list.


# You can do just about anything with each item in a for loop:
cars = ['audi', 'honda', 'fiat', 'ferrari']
for car in cars:
    print(f"{car.title()} is awsome.")
# You can also write as many lines of code as you like in the for loop. Every indented line following
# the line for car in cars is considered inside the loop, and each indented line is executed once for
# each value in the list.
    print(f"I can't wait to see {car.title()}'s new model.\n")


# DOING SOMETHING AFTER A FOR LOOP
# Any lines of code after the for loop that are not indented are executed once without repetition.
phones = ['iPhone', 'Samsung', 'Huawei']
for phone in phones:
    print(f"{phone} is really good.")
    print(f"I am curious what will be next from {phone}.\n")

print(f"Thanks to all developers and designers for making them really good.")


# MAKING NUMERICAL LISTS AND USING THE range() FUNCTION
# Python's range() function makes it easy to generate a series of numbers. It causes Python to start
# counting at the first value you give it, and it stops when it reaches the second value you provide.
for value in range(1, 5):
    print(value)


# USING range() TO MAKE A LIST OF NUMBERS
# You can convert the results of range() directly into a list using the list() function. When you wrap
# list() around a call to the range() function, the output will be a list of numbers.
numbers = list(range(1, 6))
print(numbers)

# You can also use the range() function to tell Python to skip numbers in a given range. If you pass a
# third argument to range(), Python uses that value as a step size when generating numbers. For example
# here's how to list the even numbers between 1 and 10:
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# For example, consider how you might make a list of the first 10 square numbers (that is, the square of
# each integer from 1 through 10). In Python, two asterisks(**) represent exponents. Here's how you might
# put the first 10 square numbers into a list:
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)


# SIMPLE STATISTICS WITH A LIST OF NUMBERS
# A few Python functions are helpful when working with lists of numbers. You can easily find the minimum, 
# maximum, and sum of a list of numbers:
list_of_numbers = []
for number in range(1, 13):
    list_of_numbers.append(number)
print(min(list_of_numbers))
print(max(list_of_numbers))
print(sum(list_of_numbers))


# LIST COMPREHENSIONS
# A list comprehension combines the for loop and the creation of new elements into one line, and automatically
# appends each new element. The following example builds the same list of square numbers we used earlier but now 
# we use a list comprehension:
squares = [value**2 for value in range(1, 11)]
print(squares)


# SLICING A LIST
# To make a slice, you specify the index of the first and last elements you want to work with. As with the range()
# function, Python stops one item before the second index you specify.
random_names = ['james', 'may', 'eric', 'monica']
print(random_names[1:3])

# If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list:
print(random_names[:3])

# Similar syntax works if you want a slice that includes the end of the list:
print(random_names[2:])

# You can output any slice from the end of a list with a negative index:
print(random_names[-2:])

# NOTE: You can include a third value in the brackets indicating a slice. If a third value is included, this tells 
#       Python how many items to skip between items in the specified range.


# LOOPING THROUGH A SLICE
# You can use a slice in a for loop if you want to loop through a subset of the elements in a list.
players = ['ronaldo', 'messi', 'xavi', 'iniesta', 'ibrahimovic']

print("Here are first two players on my team:")
for player in players[:2]:
    print(player.title())


# COPYING A LIST
# To copy a list, you can make a slice that includes the entire original list by omitting the first
# index and the second index ([:]). This tells Python to make a slice that starts at the first item
# and ends with the last item, producing a copy of the entire list.
foods = ['pizza', 'burek', 'falafel', 'donut']
friends_food = foods[:]

print("My favorite foods are:")
print(foods)

print("\nMy friend's favorite foods are:")
print(friends_food)


# TUPLES
# Python refers to values that cannot change as immutable, and an immutable list is called a tuple.
# A tuple looks just like a list, except you use parentheses instead of square brackets. Once you
# define a tuple, you can access individual elements by using each item's index, just as you would
# for a list.
countries = ('USA', 'Ireland')
print(countries[0])
print(countries[1])

# NOTE: Tuples are technically defined by the presence of a comma; the parentheses make them look
#       neater and more readable. If you want to define a tuple with one element, you need to include
#       a trailing comma: my_tuple = (3,). It doesn't often make sense to build a tuple with one element,
#       but this can happen when tuples are generated automatically.


# LOOPING THROUGH ALL VALUES IN A TUPLE
# You can loop over all the values in a tuple using a for loop.
for country in countries:
    print(country)


# WRITING OVER A TUPLE
# You can't modify a tuple, you can assign a new value to a variable that represents a tuple.
print("Original countries:")
for country in countries:
    print(country)

countries = ('France', 'Spain')
print("\nModified countries:")
for country in countries:
    print(country)
# Python doesn't raise any errors this time, because reassigning a variable is valid. When
# compared with lists, tuples are simple data structures. Use the when you want to store a
# set of values that should not be changed throughout the life of a program.