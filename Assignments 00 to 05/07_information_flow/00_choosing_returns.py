# Fill out the is_adult(age) function, which returns True if the function takes an age that is greater than or equal to ADULT_AGE. 
# If the function takes an age less than ADULT_AGE, return False instead.
ADULT_AGE = 18
def is_adult(age):
    return age >= ADULT_AGE
age = int(input("How old you are?"))
print(is_adult(age))