# Fill out print_multiple(message, repeats), which takes as parameters a string message to print.
# And an integer repeats number of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.
def print_multiple(message, times):
    for i in range(times):
        print(message)

def main():
    message = input("Enter a message: ")
    times = int(input("How many times do you want to print it? "))
    print_multiple(message, times)
if __name__ == "__main__":
    main()
