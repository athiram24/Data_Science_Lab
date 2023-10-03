#program to validate password
import re

def isvalid(password):
    if(len(password)<6):
        return False
    if not re.search(r'[@$%]',password) and not re.search(r'[0-9]',password):
        return False

    if not re.search(r'[a-z]',password):
        return False
    if not re.search(r'[A-Z]',password):
                return False
    return True
adhiM 

password = input("Enter a password:")
if(isvalid(password)):
    print("Valid")
else:
    print("Invalid")

        
