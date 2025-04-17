# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly.
# Note that you can call input() with no prompt and it will still wait for a user to type something!

AFFIRMATION = "You're doing great! Keep it up!"
def wholesome_machine():
    print(f"Please type the following affirmation {AFFIRMATION}:")
    while True:
     user_input = input()
     if user_input == AFFIRMATION:
         print("Great job! You're doing amazing!")
         break
     else:
         print("That's okay! Just keep trying!")
wholesome_machine()



    
