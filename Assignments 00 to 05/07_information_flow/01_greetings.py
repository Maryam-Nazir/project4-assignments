# We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting.
# Write some code in main() to get the user's name and then greet them, being sure to call the greet(name) helper function.
def greetings(name:str) -> str:
    return f"Greetings {name}"
name = input("What's your name? ")
print(greetings(name))


