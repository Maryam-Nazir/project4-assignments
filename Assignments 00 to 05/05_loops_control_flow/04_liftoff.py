# Write a program that prints out the calls for a spaceship that is about to launch.
# Countdown from 10 to 1 and then output Liftoff!
import time
def Liftoff():
    for i in range(10,0,-1):
        print(i,)
        time.sleep(1)
    print("Liftoff!")
Liftoff()




