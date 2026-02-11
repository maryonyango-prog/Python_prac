import os
def listFolderFiles(folder_path):
    files = os.listdir(folder_path)
    print(f"Files in the folder: {files}")
    return files