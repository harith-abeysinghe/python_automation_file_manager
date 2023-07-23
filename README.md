
#**Python Automation File Manager**
This Python script provides a simple and efficient file organizer tool that helps you manage and categorize your files into specific folders based on their file types. The script utilizes the popular tkinter library for user interaction, allowing you to choose the source folder containing the files to organize and the destination folder where the categorized files will be moved.

#**How it Works**
The script prompts you to select the source folder from which you want to organize files.

It then scans the source folder to retrieve a list of all the files present in it.

Next, you are prompted to choose the destination folder where the categorized files will be moved.

The script then defines a function, copy_file, which copies each file from the source to the appropriate destination folder based on its file type. After copying, the original file is removed from the source folder.

The script categorizes files into different folders based on their file extensions. Supported file types include:

Images: .jpg, .png, .jpeg
PDF: .pdf
Zipped Files: .zip, .rar
Documents: .doc, .docx, .txt
Excel: .xls, .xlsx
Videos: .mp4, .mkv, .webm
Software: .exe
For each file in the source folder, the script identifies its file type and moves it to the corresponding folder in the destination directory.

#**How to Use**
Clone or download the repository containing the script to your local machine.
Ensure you have Python installed (Python 3.x is recommended).
Run the script in your preferred Python environment.
When prompted, select the source folder containing the files you want to organize.
Next, select the destination folder where the categorized files will be moved.
The script will then create specific folders for each supported file type within the destination folder (if they don't exist already).
Files will be moved from the source folder to their respective folders in the destination directory based on their file extensions.
