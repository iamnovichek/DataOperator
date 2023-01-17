import os
from functions import *


current_directory = os.getcwd()
data_storage = "UsersData.json"


while True:

    print("Enter 1 to update data\n\nEnter 2 to get data\n\nEnter 3 to delete data\n\nEnter 4 to exit\n\n")

    program_mode = input()
 
    # --> updating data
    if program_mode == "1":
        
        update_data()
        continue

    # --> get information about user
    if program_mode == "2":

        print("Enter user name to get information about this user\n")
        
        username = input()

        find_user(username)
        continue

    if program_mode == "3":
        
        print("Enter user name to delete information\n\n")
        
        username = input()

        while (True):

            if delete_user(username) == True:
                break
            
            elif delete_user(username) == False:
                break
            
            else:
                continue
        
        continue
                 
    if program_mode == "4":
        break

    else:
        print("Input ERROR!")
        continue
