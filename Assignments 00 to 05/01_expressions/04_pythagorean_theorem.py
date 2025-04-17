#In a right triangle,the square of the hypotenuse is equal to the sum of the square of the other two sides.
#let's consider a right triangle ABC,with the right angle located at C. 
#According to the Pythagorean theorem:
#BC ** 2 = AB ** 2 + AC ** 2
import math
def main():
    ab: float = float(input("Enter the length of AB:"))
    ac: float=  float(input("Enter the length of AC:"))
# Calculate the hypotenuse using the two sides and print it out
    bc: float = math.sqrt(ab**2 + ac**2)
    print("The length of BC (the hypotenuse) is: " + str(bc))
main()

#Output
#length of AB: 3
#length of AC: 4
#The length of BC (the hypotenuse) is: 5.0