# Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!
import time
def liftoff(start_Value,end_Value,jumped_value):
    for i in range(start_Value,end_Value,-jumped_value):
       time.sleep(1)
       print(i)
       
def main():
    start_Value = int(input("Enter a start Value"))
    end_Value = int(input("Enter a start Value"))
    jumped_value = int(input("Enter a start Value"))
    liftoff(start_Value,end_Value,jumped_value)
main()