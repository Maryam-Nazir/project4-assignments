# Implement the helper function make_sentence(word, part_of_speech) which will take a string word and an integer part_of_speech as parameters and, depending on the part of speech, place the word into one of three sentence templates (or one from your imagination!):

def make_sentence(word, part_of_speech):
# If part_of_speech is 0, we will assume the word is a noun and use the template: 
# "I am excited to add this ____ to my vast collection of them!"
    if part_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
# If part_of_speech is 1, we will assume the word is a verb use the template: "It's so nice outside today it makes me want to ____!"
    elif part_of_speech == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
# If part_of_speech is 2, we will assume the word is an adjective and use the template: "Looking out my window, the sky is big and ____!" make_sentence(word, part_of_speech) should not return anything, just print the correct sentence with the word filled in the blank.
    elif part_of_speech == 2:
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Oops! That part of speech is not recognized.")

def main():
    word = input("Please type a noun, verb, or adjective: ")
    part = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(word, part)

if __name__ == "__main__":
    main()

