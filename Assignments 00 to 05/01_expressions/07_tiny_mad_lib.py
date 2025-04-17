#Write a program which prompts the user for an adjective,a noun,then a verb,and then prints a fun sentence.
SENTENCE_START: str = "Code in place is fun. I learned to program and used python to make my "
def main():
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter .")
    verb: str = input("Please type a verb and press enter.")
    print(SENTENCE_START + adjective + " " + noun + "" +verb + "!")
main()
 
#Output
#Code in Place is fun. I learned to program and used Python to make my tiny plant fly!