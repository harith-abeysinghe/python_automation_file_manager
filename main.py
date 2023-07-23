import os
import shutil
from tkinter.filedialog import askdirectory

#Selcting source folder
source_path = askdirectory(title="Select Source")

#Getting all files in source
files = os.listdir(source_path)

#Selcting destination folder
destination_path = askdirectory(title="Select Destination")

# Create a new directories for different file types
directory_names = ["PDF", "Video","Zipped Files", "Word Documents", "Excel", "Images"]
for directory_name in directory_names:
    try:
        destination_folder = os.path.join(destination_path, directory_name)
        os.mkdir(destination_folder)
        print("Directory Created: " + directory_name)
    except FileExistsError:
        print("Directory Exists: " + directory_name)

# for file in files:
#     print()
#     print(file)
#     Create the full source file path
    # source_file_path = os.path.join(source_path, file)
    #
    # Create the full destination file path
    # destination_file_path = os.path.join(destination_path, file)
    #
    # try:
    #     Copy the file from source to destination
        # print(f"Copying: {file}")
        # shutil.copy(source_file_path, destination_file_path)
        # print(f"Copied: {file}")
    # except PermissionError as e:
    #     print(f"Permission denied for {file}. Skipping...")

