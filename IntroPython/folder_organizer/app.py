from user_folder import get_user_folder_path
from file_sys import listFolderFiles

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

    
main()

