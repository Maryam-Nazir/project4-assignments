#  Fill out the get_user_data() function which:
# Asks the user for their first name and stores it in a variable
# Asks the user for their last name and stores it in a variable
# Asks the user for their email address and stores it in a variable
def get_user_data():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your enail address: ")
    return first_name, last_name, email
print("Please enter your details:")
user_data = get_user_data()
print("Received the following user data:", user_data)