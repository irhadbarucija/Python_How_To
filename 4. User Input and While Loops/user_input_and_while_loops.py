# HOW THE input() FUNCTION WORKS
# The input() function pauses your program and waits for the user to enter some text. Once the Python receives
# the user's input, it assigns that input to a variable to make it convenient for you to work with.
prompt = ("If you tell us your name, we can find you in our database. ")
prompt += ("\nYour name is? ")

name = input(prompt)
print(f"\nHello, {name.title()}!")


# USING int() TO ACCEPT NUMERICAL INPUT
# When you use the input() function, Python interprets everything the user enters as a string. By using the int()
# function, Python converts the input string to a numerical value so we can run comparison successfully.
age = input("\nHow old are you? ")
age = int(age)

if age >= 18:
    print("\nYou're old enough to drive.")
else:
    print("\nSorry, you'll need to wait a bit for driving lessons.")


# THE MODULO OPERATOR
# Modulo operator % divides one number by another number and returns the remainder. When one number is divisible by
# another number, the remainder is 0, so the modulo operator always returns 0. You can use this fact to determine 
# if a number is even or odd.
number = input("\nEnter a number so we check if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")


# THE WHILE LOOP
# The while loop runs as long as, or while, a certain condition is true.
prompt = "\nTell me something and I will repeat it! "
prompt += "\nEnter 'exit' to end the program. "

message = ""
while message != 'exit':
    message = input(prompt)

    if message != 'exit':
        print(message)


# USING A FLAG
# For a program that should run only as long as many conditions are true, you can define one variable that determines
# whether or not the entire program is active. This variable, called a flag, acts as a signal to the program. We can
# write our programs so they run while while the flag is set to True and stop running when any of several events sets
# the value of the flag to False.
prompt = "\nWith flag. Tell me something and I will repeat it! "
prompt += "\nEnter 'exit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'exit':
        active = False
    else:
        print(message)


# USING break TO EXIT A LOOP
# To exit a while loop immediately without running any remaining code in the loop, regardless of the results of any 
# conditional test, use the break statement. The break statement directs the flow of your program; you can use it to
# control which lines of code are executed and which aren't, so the program only executes code that you want it to, 
# when you want it to.
prompt = "\nPlease enter your dream car: "
prompt += "\nEnter 'exit' when you are done. "

while True:
    car = input(prompt)

    if car == 'exit':
        break
    else:
        print(f"My dream car is {car.title()}!")

# NOTE: You can use the break statement in any of Python's loops. For example, you could use break to quit a for loop
#       that's working through a list or a dictionary.


# USING continue IN A LOOP
# Rather than breaking out of a loop entirely without executing the rest of its code, you can use the continue statement
# to return to the beginning of the loop, based on the result of a conditional test.
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)


# USING A while LOOP WITH LISTS AND DICTIONARIES
# A for loop is effective for looping through a list, but you shouldn't modify a list inside a for loop because Python 
# will have trouble keeping track of the items in the list. To modify a list as you work through it, use a while loop. 
# Using while loops with lists and dictionaries allows you to collect, store, and organize lots of input to examine and
# report on later.


# MOVING ITEMS FROM ONE LIST TO ANOTHER
owned_cars = ['fiat grande punto', 'peugeot 206', 'alfa romeo 147']
sold_cars = []

while owned_cars:
    current_car = owned_cars.pop()

    print(f"The {current_car.title()} is on sale!")
    sold_cars.append(current_car)

print(f"\nThe following cars has been sold: ")
for car in sold_cars:
    print(car.title())


# REMOVING ALL INSTANCES OF SPECIFIC VALUES FROM A LIST
pets = ['dog', 'cat', 'snake', 'dog', 'fish', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


# FILLING A DICTIONARY WITH USER INPUT
responses = {}

poll_active = True

while poll_active:
    name = input("\nWhat is your name? ")
    response = input("\nWhich country would you like to visit? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        poll_active = False

for name, response in responses.items():
    print(f"\n{name.title()} would like to visit {response.title()}.")