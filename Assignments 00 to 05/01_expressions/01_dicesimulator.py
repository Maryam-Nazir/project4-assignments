#Import the random library which lets us simulate random things like dice!
import random
# Number of sides on each die to roll
one_side = 6

def roll_dice():
 die1 = random.randint(1, one_side)
 die2 = random.randint(1, one_side)
 total = die1 + die2
 print(f"Total of the two dice {total}")
def main():
 die1 = 10
 print("die1 in main() starts as: " + str (die1))
 roll_dice()
 roll_dice()
 roll_dice()
 print("die1 in main() starts as:" + str (die1))
main()



