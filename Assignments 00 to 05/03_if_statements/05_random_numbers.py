# Print 10 random numbers in the range 1 to 100.
import random
def main():
    for i in range(10):
        gen = random.randint(1,100)
        print(gen, end=" ")
main()