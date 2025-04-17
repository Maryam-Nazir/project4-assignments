# Converting the Earthing's weight from a string to a number so we can do math with it. We use the float function to do this, since the weight isn't necessarily a whole number.
# Calculating the weight on Mars, which we do by multiplying the Earth weight by 0.378. 
# To make the program easy to read, we store this number in a constant called MARS_MULTIPLE.

def calculate(earth_weight,planet):
     if planet == "mercury":
         return earth_weight *0.376
     elif planet == "venus":
         return earth_weight *889
     elif planet == "mars":
         return earth_weight *0.378
     elif planet == "jupiter":
         return earth_weight *2.36
     elif planet == "saturn":
         return earth_weight *1.081
     elif planet == "uranus":
         return earth_weight *0.815
     elif planet == "neptune":
         return earth_weight *1.14
earth_weight = float(input("Enter a earth weight: "))
planet = input("Enter a planet weight: ").lower()
res = calculate(earth_weight,planet)
print(res)