import os
import shutil
from tkinter.filedialog import askdirectory

source_path = askdirectory(title="Select Source")

files = os.listdir(source_path)
destination_path = askdirectory(title="Select Destination")
for file in files:
    print()
    print(file)
    # Create the full source file path
    source_file_path = os.path.join(source_path, file)

    # Create the full destination file path
    destination_file_path = os.path.join(destination_path, file)

    try:
        # Copy the file from source to destination
        shutil.copy(source_file_path, destination_file_path)
        print(f"Copied: {file}")
    except PermissionError as e:
        print(f"Permission denied for {file}. Skipping...")

