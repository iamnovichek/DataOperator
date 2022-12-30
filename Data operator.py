import json
import os
from pprint import pprint
from functions import *

# get current dir
current_directory = os.getcwd()
file_name = "UsersData.json"

# try to find "JSON" file
try:
    with open(f"{current_directory}/{file_name}", "r") as f:
        
        data = json.load(f)
# if it does not exist
# --> create it
except:
    
    with open(f"{current_directory}/{file_name}", "w") as f:

        meta = dict()
        f.write(json.dumps(meta))


# our program 
while True:

     # Enter a number to choose program mode
    print("Enter 1 to update data\n\nEnter 2 to get data\n\nEnter 3 to delete data\n\nEnter 4 to exit\n\n")
    program_mode = input()
 
    # --> updating data
    if program_mode == "1":
        
        user_data = enter_data()
        
        with open(f"{current_directory}/{file_name}","r") as js:
        
            data = json.load(js)

        data.update(user_data)

        with open(f"{current_directory}/{file_name}","w") as jso:
        
            jso.write(json.dumps(data,indent=2))

        continue

    # --> get information about user
    if program_mode == "2":

        print("Enter user name to get information about this user\n")
        
        find_user = input()

        with open(f"{current_directory}/{file_name}","r") as js:
    
            data = json.load(js)

        for item in data:
                    
            if item == find_user:    
                print("=="*15)
                print(f"{find_user}:")
                pprint(data[find_user])
                print("=="*15)

        if find_user not in data:
            print("User not found: try again!")

        continue

    if program_mode == "3":
        
        print("Enter user name to delete information\n\n")
        
        find_user = input()

        with open(f"{current_directory}/{file_name}","r") as js:
    
            data = json.load(js)

        passw = input("Enter user's password to confirm!\n\n")

        if passw != data[find_user]["Password"]:

            print("Password is not correct!\n\n")
            continue

        del data[find_user]

        with open(f"{current_directory}/{file_name}","w") as jso:
            
            json.write(json.dumps(data,indent=2))
        
        print(f"User: \"{find_user}\" has been successful deleted!\n")
        continue
                 
    if program_mode == "4":
        break

    else:
        print("Input ERROR!")
        continue
