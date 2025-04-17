# Mad libs Python Project:
# Get input from the user, work with f-strings, and see your results printed to the console.
def Mad_Libs_Game():
    name = input("Enter your name: ")
    place = input("Enter a place name: ")
    animal = input("Enter a animal name:")
    verb = input("Enter an action (verb): ")
    adjective = input("Enter an adjective: ")

    print("\nAll inputs are saved! ✅")
    story = f"One day, {name} went to {place}. There, they saw a {adjective} {animal} that was {verb}. Seeing this, {name} was very surprised!"
    print("\nHere is your funny story:\n")
    print(story)
Mad_Libs_Game()



