import os
import shutil
from collections import defaultdict
from plyer import notification  # For notifications

def organize_files(source_folder, destination_folder):
    # Define file type categories
    file_types = {
        "Images": [".jpeg", ".jpg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv"],
        "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
        "Compressed": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Programs": [".exe", ".msi"],
        "Others": []  # For files that do not match the above types
    }

    # Create folders in the destination if not exists
    for folder in file_types:
        os.makedirs(os.path.join(destination_folder, folder), exist_ok=True)

    # Classify files and move them
    files_moved = defaultdict(int)
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file_name)[1].lower()
            moved = False

            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    shutil.move(file_path, os.path.join(destination_folder, folder, file_name))
                    files_moved[folder] += 1
                    moved = True
                    break

            if not moved:  # If no matching type, move to 'Others'
                shutil.move(file_path, os.path.join(destination_folder, "Others", file_name))
                files_moved["Others"] += 1

    return files_moved

if __name__ == "__main__":
    # Define source folders (multiple sources supported)
    source_folders = [
        os.path.expanduser("~/Downloads")  # Default Downloads folder
        # Add more source folders as needed
    ]
    destination_folder = "D:\\From Downloads"

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    total_files_moved = defaultdict(int)
    for source_folder in source_folders:
        if os.path.exists(source_folder):
            print(f"Processing files from: {source_folder}")
            files_moved = organize_files(source_folder, destination_folder)
            for folder, count in files_moved.items():
                total_files_moved[folder] += count
        else:
            print(f"Source folder not found: {source_folder}")

    # Print summary
    print("\nFile organization completed!")
    for folder, count in total_files_moved.items():
        print(f"{count} file(s) moved to {folder}.")

    # Send a notification
    notification.notify(
        title="File Organization Complete",
        message=f"Files from all source folders have been organized into {destination_folder}.",
        app_name="File Organizer",
        timeout=10  # Notification timeout in seconds
    )
