import os
import sys

def get_user_folder_path():
    folder_path = input("Please enter the path of the folder you want to organize: ")
    print(f"You entered: {folder_path}")
    isdir = os.path.isdir(folder_path)

    if not isdir:
        print("The path you entered is not a valid directory. ")
        sys.exit()
    return folder_path