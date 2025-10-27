# CONDITIONAL TESTS
# At the heart of every if statement is an expression that can be evaluated as True or False and is called a conditional test. Python uses the
# the values True or False to decide whether the code in an if statement should be executed. 


# COMPARISON OPERATORS
# Comparison operators we are using in Python:
#                                              == Equal to
#                                              != Not equal to
#                                              <  Less than
#                                              >  Greater than
#                                              <= Less than or equal to
#                                              >= Greater than or equal to


# CHECKING FOR EQUALITY
# The simplest conditional test checks whether the value of a variable is equal to the value of interest:
car = 'bmw'
if car == 'bmw':
    print("It's equal!")
else:
    print("Sorry, values are not matching!")
# Two values with different capitalization are not considered equal. However you can use the lower() method
# that doesn't change the value, only so you can do comparison without affecting the original variable.


# CHECKING FOR INEQUALITY
# When you want to determine whether two values are not equal, you can use the inequality operator (!=).
requested_ingredients = 'mozzarella'

if requested_ingredients != 'mushrooms':
    print("We only have Mozzarella!")


# NUMERICAL COMPARISONS
# You can include various mathematical comparisons in your conditional statements as well, such as less than
# less than or equal to, greater than, and greater than or equal to:
number = 22
if number <= 34:
    print("That is lower than expected!")


# CHECKING MULTIPLE CONDITIONS
# You may want to check multiple conditions at the same time. The keywords 'and' and 'or' can help you in these situations.
# If we use 'and' then each test must pass so it evaluates to True, if either tests fail, the expression evaluates to False.
number = 31
if number <= 32 and number >= 18:
    print("You got this!")
# The keyword 'or' allows you to check multiple conditions as well, but it passes when either or both of the individual
# tests fail.
number = 18
if number <= 16 or number >= 18:
    print("Do not get confused!")


# CHECKING WHETHER A VALUE IS IN A LIST OR NOT
# Sometimes it's important to check whether a list contains a certain value before taking an action. If that's the case use 
# the keyword 'in'. Other times, you can use the keyword 'not' if it's important to know if a value
# does not appear in a list.
existing_users = ['sasuke', 'rock lee', 'naruto']
print(existing_users)
new_user = 'sakura'

if new_user not in existing_users:
    existing_users.append(new_user)
print(f"We have a new member in our team. Say hello to {new_user.title()}!")
print(existing_users)


# BOOLEAN EXPRESSIONS
# A Boolean expression is just another name for a conditional test. A Boolean value is either True or False, just like the 
# value of a conditional expression after it has been evaluated.


# SIMPLE if STATEMENTS
# # Python's if statements allows you to examine the current state of a program and respond appropriately to that state. 
# Here is a simple example:
cars = ['honda', 'bmw', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())


# if-else STATEMENTS
# An if-else block is similar to a simple if statement, but the else statement allows you to define an action or set of 
# actions that are executed when the conditional test fails.
age = 17

if age >= 18:
    print("You are old enough to drive!")
else:
    print("Sorry, you are not old enough to drive!")


# THE if-elif-else CHAIN
# Python executes only one block in an if-elif-else chain. It runs each conditional test in order, the code following
# that test is executed and Python skips the rest of the tests.
age = 14

if age < 4:
    print("Bus ticket is free.")
elif age < 18:
    print("Bus ticket is 10$.")
else:
    print("Bus ticket is 18$.")


# USING MULTIPLE elif BLOCKS
# You can use as many elif blocks in your code as you like.
age = 15

if age < 4:
    price = 0
elif age > 4 and age < 18:
    price = 10
elif age > 18 and age < 65:
    price = 18
else:
    price = 15

print(f"The price of your bus ticket is {price}$.")


# OMITTING THE else BLOCK
# Python does not require an else block at the end of an if-elif chain. Sometimes, an else block is useful. Other times, it's
# clearer to use an additional elif statement that catches the specific condition of interest.
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is {price}$.")
# The else block is a catchall statement. It matches any condition that wasn't matched by a specific if or elif test, and that 
# can sometimes include invalid or even malicious data. If you have a specific final condition you're testing for, consider using
# a final elif block and omit the else block.


# TESTING MULTIPLE CONDITIONS
# The if-elif-else chain is powerful, but it's only appropriate to use when you just need one test to pass. However, sometimes it's 
# important to check all conditions of interest. In this case, you should use a series of simple if statements with no elif or else blocks.
requested_drinks = ['water', 'coffee']

if 'water' in requested_drinks:
    print("Adding water.")
if 'sparkling water' in requested_drinks:
    print("Adding sparkling water.")
if 'coffee' in requested_drinks:
    print("Adding coffee.")

print(f"Finished you order!")
# In summary, if you want only one block of code to run, use an if-elif-else chain. If more than one block of code needs to run, use a series
# of independent if statements.


# USING if STATEMENTS WITH LISTS
# You can do some interesting work when you combine lists and if statements. You can watch for special values that need to be treated differently
# than other values in the list. You can efficiently manage changing conditions, such as the availability of certain items.
requested_ingredients = ['mushrooms', 'salami', 'onion', 'cheese']

for requested_ingredient in requested_ingredients:
    if requested_ingredient == 'onion':
        print("Sorry, we are out of onions right now.")
    else:
        print(f"Adding {requested_ingredient}")

print("\nFinished making your pizza!")


# CHECKING THAT A LIST IS NOT EMPTY
# It's useful to check whether a list is empty before running a for loop.
requested_ingredients = []

if requested_ingredients:
    for requested_ingredient in requested_ingredients:
        print(f"\nAdding {requested_ingredient}")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want only dough?")


# USING MULTIPLE LISTS
available_cars = ['Audi A3', 'BMW M5', 'Citroen C3', 'Peugeot 3008', 'Toyota Supra']
requested_cars = ['Audi A3', 'Renault Clio', 'Honda Civic Type-R']

for requested_car in requested_cars:
    if requested_car in available_cars:
        print(f"\nAdding {requested_car}!")
    else:
        print(f"Sorry, we don't have {requested_car}.")

print("\nYour cars are ready.")