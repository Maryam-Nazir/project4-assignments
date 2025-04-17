# Print 10 random numbers in the range 1 to 100.
import random
def print_random_number():
    for _ in range(10):
        print(random.randint(1,100),end=" ")
print_random_number()