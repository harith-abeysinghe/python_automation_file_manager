import os
import shutil
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
from tkfilebrowser import askopendirnames

folder_extenstions = {
    "Images": ['.jpg', '.png', '.jpeg'],
    "PDF": [".pdf"],
    "Zipped Files": [".zip", ".rar"],
    "Documents": [".doc", ".docx", ".txt"],
    "Excel": [".xls", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".webm"],
    "Software": [".exe", ".msi"]
}

class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")

        self.folders = []
        self.destination_path = ""

        self.select_folders_btn = ttk.Button(root, text="Select Folders", command=self.select_folders)
        self.select_folders_btn.pack(pady=10)

        self.select_destination_btn = ttk.Button(root, text="Select Destination", command=self.select_destination)
        self.select_destination_btn.pack(pady=5)

        self.organize_btn = ttk.Button(root, text="Organize Files", command=self.organize_files)
        self.organize_btn.pack(pady=10)

        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.pack(padx=10, pady=10)

    def select_folders(self):
        self.folders = askopendirnames()

    def select_destination(self):
        self.destination_path = askdirectory(title="Select Destination")
        self.output_text.insert(tk.END, f"Destination selected: {self.destination_path}\n")

    def organize_files(self):
        if self.destination_path and self.folders:
            directory_names = ["PDF", "Videos", "Zipped Files", "Documents", "Excel", "Images", "Software"]
            for directory_name in directory_names:
                try:
                    destination_folder = os.path.join(self.destination_path, directory_name)
                    os.makedirs(destination_folder, exist_ok=True)
                    self.output_text.insert(tk.END, f"Directory Created: {directory_name}\n")
                except FileExistsError:
                    self.output_text.insert(tk.END, f"Directory Exists: {directory_name}\n")

            for source_path in self.folders:
                files = os.listdir(source_path)
                for file in files:
                    for folder, extensions in folder_extenstions.items():
                        self.select_file_type(folder, extensions, source_path, file)

    def select_file_type(self, folder_name, extensions, source_path, file):
        if any(file.lower().endswith(extension) for extension in extensions):
            source_file_path = os.path.join(source_path, file)
            destination_file_path = os.path.join(self.destination_path, folder_name, file)
            self.copy_file(source_file_path, destination_file_path)

    def copy_file(self, source_file_path, destination_file_path):
        try:
            shutil.copy(source_file_path, destination_file_path)
            os.remove(source_file_path)
            self.output_text.insert(tk.END, f"Copied: {source_file_path} to {destination_file_path}\n")
        except PermissionError:
            self.output_text.insert(tk.END, f"Permission denied for {source_file_path}. Skipping...\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()
