# PASSING A LIST

# When you pass a list to a function, the function gets direct access to the contents
# of the list.
def feed_pets(names):
    """Print a simple name list of pets that you need to feed."""
    for name in names:
        msg = f"Are you hungry, {name.title()}?"
        print(msg)

pet_names = ['mona', 'sumsirka', 'simba']
feed_pets(pet_names)


# Modifying a List in a Function

# When you pass a list to a function, the function can modify the list. Any changes made 
# to the list inside the function's body are permanent, allowing you to work efficiently
# even when you're dealing with large amounts of data.
def new_songs(unfinished_songs, finished_songs):
    """Simulate finishing each song. Move each song to finished_songs after printing."""

    while unfinished_songs:
        current_song = unfinished_songs.pop()
        print(f"\nFinishing song: {current_song}!")
        finished_songs.append(current_song)

def show_new_songs(finished_songs):
    """Show all the songs that were in the list."""
    print(f"\nThe following songs have been recorded:")
    for finished_song in finished_songs:
        print(finished_song)

unfinished_songs = ['autumn', 'good night', 'solar']
finished_songs = []

new_songs(unfinished_songs, finished_songs)
show_new_songs(finished_songs)


# Preventing a Function from Modifying a List
# For example we will use function from above new_songs:
new_songs(unfinished_songs[:], finished_songs)
# The slice notation [:] makes a copy of the list to send to the function.


# PASSING AN ARBITRARY NUMBER OF ARGUMENTS
# Sometimes you won't know ahead of time how many arguments a function needs to accept.
# Python allows a function to collect an arbitrary number of arguments from the calling
# statement.
def make_sentence(*words):
    """Print the list of words that you want to make a sentence."""
    print("\nMaking a sentence with the following words:")
    for word in words:
        print(f"{word}")

make_sentence('hi')
make_sentence('I', 'want', 'to', 'get', 'a', 'job', 'as', 'a', 'python', 'developer')


# Mixing Positional and Arbitrary Arguments
# If you want a function to accept several different kinds of arguments, the parameter that
# accepts an arbitrary number of arguments must be placed last in the function definition. 
# Python matches positional and keyword arguments first and then collects any remaining arguments
# in the final parameter.
def make_sentence(size, *words):
    """Print the list of words that you want to make a sentence."""
    print(f"\nMaking a sentence with {size} words:")
    for word in words:
        print(f"{word}")

make_sentence(4, 'I', 'want', 'some', 'food')


# Using Arbitrary Keyword Arguments
# Python can accept an arbitrary number of arguments, but you won't know ahead of time what kind 
# of information will be passed to the function.
def build_profile(first, last, **user_info):
    """A dictionary  containing  everything we know about a user."""
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

user_profile = build_profile('mona', 'labrador', location='sarajevo', animal='dog')
print(user_profile)