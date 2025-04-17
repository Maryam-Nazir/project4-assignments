# Converts feet to inches.There are 12 inches per foot.
# Feet is an American unit of measurement.
INCHES_IN_FOOT: int = 12
def main():
    feet: float = float(input("Enter number of feet:"))
    inches: float = feet * INCHES_IN_FOOT              # 12 inches = 1 foot
    print("That is",inches, "inches!" )
    
main()


