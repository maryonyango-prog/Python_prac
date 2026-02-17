from user_folder import get_user_folder_path
from file_sys import listFolderFiles
import os

IMAGES = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
MUSIC = ['.mp3', '.wav', '.aac', '.flac']
PDFS = ['.pdf', '.docx', '.txt', '.xlsx']
ZIP = ['.zip', '.rar', '.tar', ]
def main():
    print("Welcome to the Folder Organizer!")
    print("_________________________________")
    working_folder = get_user_folder_path()
    item_list = listFolderFiles(working_folder)

    for item in item_list:
        print(f"Single item is: {item}")
        split_item = os.path.splitext(item)

        print(f"Split item is: {split_item}")

        print(f"First element is: {split_item[0]}")

        print(f"Second element is: {split_item[1]}")

        extension = split_item[1]
        if extension in IMAGES:
            print("This is an image file.")
            
        elif extension in MUSIC:
            print("This is a music file.")

        elif extension in PDFS:
            print("This is a PDF file.")

        elif extension in ZIP:
            print("This is a ZIP file.")

        else:
            print("This file type is not recognized.")

    
main()

