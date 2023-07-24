## Python Automation File Manager

This Python script provides a simple and efficient file organizer tool that helps you manage and categorize your files into specific folders based on their file types. The script utilizes the popular `tkinter` library for user interaction, allowing you to choose the source folder containing the files to organize and the destination folder where the categorized files will be moved.

### How it Works

1. The script prompts you to select the source folder from which you want to organize files.
2. It then scans the source folder to retrieve a list of all the files present in it.
3. Next, you are prompted to choose the destination folder where the categorized files will be moved.
4. The script then defines a function, `copy_file`, which copies each file from the source to the appropriate destination folder based on its file type. After copying, the original file is removed from the source folder.
5. The script categorizes files into different folders based on their file extensions. Supported file types include:

   - **Images**: `.jpg`, `.png`, `.jpeg`
   - **PDF**: `.pdf`
   - **Zipped Files**: `.zip`, `.rar`
   - **Documents**: `.doc`, `.docx`, `.txt`
   - **Excel**: `.xls`, `.xlsx`, `.csv`
   - **Videos**: `.mp4`, `.mkv`, `.webm`
   - **Software**: `.exe`

6. For each file in the source folder, the script identifies its file type and moves it to the corresponding folder in the destination directory.

### How to Use

1. Clone or download the repository containing the script to your local machine.
2. Ensure you have Python installed (Python 3.x is recommended).
3. Run the script in your preferred Python environment.
4. When prompted, select the source folder containing the files you want to organize.
5. Next, select the destination folder where the categorized files will be moved.
6. The script will then create specific folders for each supported file type within the destination folder (if they don't exist already).
7. Files will be moved from the source folder to their respective folders in the destination directory based on their file extensions.

Please note that the script may encounter "PermissionError" for certain files if they are currently in use or protected. In such cases, those files will be skipped during the organization process.

Enjoy a clean and well-organized file system with this handy file organizer tool!
