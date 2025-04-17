# Write a program that asks a user to enter a number. 
# Your program will then double that number and print out the result. 
# Note that:
# 2 doubled is 4
# 4 doubled is 8
# 8 doubled is 16 and so on.
curr_value = int(input("Please enter a number: "))
curr_value = curr_value * 2
while curr_value < 100:
    print(curr_value)
    curr_value = curr_value * 2