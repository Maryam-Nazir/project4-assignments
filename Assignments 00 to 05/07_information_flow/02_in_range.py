# Implement the following function which takes in 3 integers as parameters:
# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """

def is_range(n,low,high):
    if n >= low and n <= high:
        return True
    return False
n = int(input("Enter a number: "))
low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))
print(is_range(n,low,high))