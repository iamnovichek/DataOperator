import re
import json
import os
import phonenumbers

# get current dir
current_directory = os.getcwd()

# --> check if phone number is valid or not
def phone_number_validation():

    while(True):
        
        valid_phone_number=phone_number = input(f"Enter phone number: ")

        if phone_number.strip() == "":

            print("Invalid number: try again!")
            continue

        else:
            try:
                phone_number = phonenumbers.parse(phone_number)

                if phonenumbers.is_valid_number(phone_number) == True:
                    return valid_phone_number
                else:
                    print("Invalid number: try again!")
            except:
                print("Invalid number: try again!") 


# --> validating an Email
def email_validation(email):
    
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    while(True):    
        if re.match(pat,email):
            return email
        else:
            print("Invalid email: try again!")
            email = input(f"Enter email: ")


# --> some rules for our first and last name
def first_and_last_name_validation(name = "",first_or_last_name = ""):

    while(True):

        check_name = ""

        if len(name) < 2:

            print("Invalid value: try again!")
            name = input(f"Enter {first_or_last_name}: ")

        for i in range(len(name)):

            if name[i] == " ":
                print("Invalid value: try again!")
                name = input(f"Enter {first_or_last_name}: ")
                break

            elif name[0].isupper() == False:

                print("Invalid value: try again!")
                name = input(f"Enter {first_or_last_name}: ")
                break

            elif name[i].isalpha() == True:
                check_name += name[i]

            else:
                print("Invalid value: try again!")
                name = input(f"Enter {first_or_last_name}: ")
                break

        if name == check_name:
            return name

# --> some rules for user name
def check_user_name(user_name):
  
    with open(f"{current_directory}/UsersData.json", "r") as f:

        data = json.load(f)
   
    while(True):

        if user_name.strip() == "":
            
            user_name = input(f"Enter user name: ")
            continue
   
        if len(user_name) < 4 or len(user_name)> 25:
            
            print("User name must be longer than 4 symbols and shorter than 25 symbols")

            user_name = input(f"Enter user name: ")
            continue     
    
        if user_name in data:

            print("User already exists!")

            user_name = input(f"Enter user name: ")
            continue
        else:
            return user_name

# takes user's password
def user_password():

    while True:

        psw = input("Enter password: ")
        symbols = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        for item in psw:
            if item.isalpha() == True:
                break
        else:
            print("The password should have letters, numbers and symbols")
            continue

        if all(char in symbols for char in psw) : # checks if all characters of pwd in symbols
            print("The password should have letters, numbers and symbols")

        elif len(psw) < 4 or len(psw) > 25:
            print("The password lenth must be between 4 et 25 symbols")

        elif psw.islower() == True:
            print("The password must have an uppercase letter")

        elif psw.isdigit() == True:
            print("The password must have letters, numbers and symboles")

        elif psw.isalpha() == True:
            print("The password must have letters, numbers and symbols")

        else:
            break

    while True:
        csw = input("Confirm your password : ")

        if csw == psw:
            break
        else:
            print("Error: try again!")

    return psw

# takes all data about user    
def enter_data ():
    
    user_name = check_user_name(input(f"Enter user name: "))

    user_data = {
        user_name :{ 
        "First name": first_and_last_name_validation(input(f"Enter first name: "),"first name"),
        "Last name": first_and_last_name_validation(input(f"Enter last name: "),"last name"),
        "Password" : user_password(),
        "Email" : email_validation(input(f"Enter email: ")),
        "Phone number" : phone_number_validation()
        }
    }

    print("=="*15)
    print("Account iformations: ")
    [print(f"{key}:{user_data.get(key)}") for key in user_data]
    print("=="*15) 
    
    return user_data
    
