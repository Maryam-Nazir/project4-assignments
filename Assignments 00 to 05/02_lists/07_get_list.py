# Write a program which continuously asks the user to enter values which are added one by one into a list.
# When the user presses enter without typing anything, print the list.
def main():
    lst = []
    val = input("Enter a value: ")
    while val:
        lst.append(val)
        val = input("Enter a value: ")
    print("Here's is the list:", lst)
main()





