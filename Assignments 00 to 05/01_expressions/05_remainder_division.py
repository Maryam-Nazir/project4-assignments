#Ask the user for two numbers,one at a time,and then print the result of dividing the first number by the second and also the remainder of the division.
def main():
    dividend: int = int(input("Please enter an integer to be divided:"))
    divisor: int =  int(input("Please enter an integer to divide by:"))
    qoutient: int = dividend // divisor
    remainder: int = dividend % divisor
    print("The result of this division is " + str(qoutient) + "with a remainder of " + str(remainder))
main()

#Output
#enter an integer to be divided: 5
#enter an integer to divide by: 3

#The result of this division is 1 with a remainder of 2