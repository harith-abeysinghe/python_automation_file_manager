import os
import shutil
from tkinter.filedialog import askdirectory

# Selecting source folder
source_path = askdirectory(title="Select Source")

# Getting all files in source
files = os.listdir(source_path)

# Selecting destination folder
destination_path = askdirectory(title="Select Destination")
print(destination_path)


# Function to copy each file
def copy_file(source_file_path, destination_file_path):
    try:
        # Copy the file from source to destination
        print(f"Copying: {file}")
        shutil.copy(source_file_path, destination_file_path)
        print(f"Copied: {file}")
        os.remove(source_file_path)
    except PermissionError as e:
        print(f"Permission denied for {file}. Skipping...")


def select_file_type(folder_name, extensions):
    for extension in extensions:
        if file.lower().endswith(extension):
            print(file)
            # Create the full source file path
            source_file_path = os.path.join(source_path, file)
            # Create the full destination file path
            destination_file_path = os.path.join(destination_path, folder_name, file)
            copy_file(source_file_path, destination_file_path)


folder_extenstions = {"Images": ['.jpg', '.png', '.jpeg'],
                      "PDF": [".pdf"],
                      "Zipped Files": [".zip", ".rar"],
                      "Documents": [".doc", ".docx", ".txt"],
                      "Excel": [".xls", ".xlsx"],
                      "Videos": [".mp4", ".mkv", ".webm"],
                      "Software" : [".exe"]
                      }
if destination_path:
    # Create a new directories for different file types
    directory_names = ["PDF", "Videos", "Zipped Files", "Documents", "Excel", "Images","Software"]
    for directory_name in directory_names:
        try:
            destination_folder = os.path.join(destination_path, directory_name)
            os.mkdir(destination_folder)
            print("Directory Created: " + directory_name)
        except FileExistsError:
            print("Directory Exists: " + directory_name)

    for file in files:
        for folder, extensions in folder_extenstions.items():
            select_file_type(folder, extensions)

