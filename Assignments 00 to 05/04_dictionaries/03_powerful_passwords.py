# Fill out the login(...) function for a website that hashes their passwords. 
# Login should return True if an email's stored password hash in stored_logins is the same as the hash of password_to_check.
from hashlib import sha256
def login(email, stored_logins, password_to_check):

    if stored_logins[email] == hash_password(password_to_check):
         return True
    
    return False

def hash_password(password):
    return sha256(password.encode()).hexdigest()
def main():
   stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc", 
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb" 
    }
   print( login("example@gmail.com",stored_logins,"123!456?789") )
main() 