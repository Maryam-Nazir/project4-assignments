# Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: Joke.
PROMPT = "What do you want? "
JOKE: str = "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY =  "Sorry I only tell jokes."
def joke_bot():
    print("Welcome to the Joke Bot!")
    user_input = input(PROMPT).lower()
    if "joke" in user_input:
        print(JOKE)
    else:
        print(SORRY)
    print("Goodbye!")
joke_bot()

