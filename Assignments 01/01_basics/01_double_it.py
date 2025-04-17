# Write a program that asks a user to enter a number. Your program will then double that number and print out the result.
# It will repeat that process until the value is 100 or greater.
def double():
    num = int(input("Enter a number: "))
    while num < 100:
        doubled = num * 2
        print(f"Double of {num} is {doubled}")
        num += num
double()