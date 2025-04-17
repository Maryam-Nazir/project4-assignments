# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.
# Assume for now that the minimum height is 50 of whatever height unit you'd like

max_hieght:int = 50
def main():
    while True:
        height = input("Enter Your Height (Press Enter to Stop):")

        if height == "":
            print("Exiting the program...")
            break
        try:
            height = int(height)
            if height >= max_hieght:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Invalid input! Please enter a number.")

main()