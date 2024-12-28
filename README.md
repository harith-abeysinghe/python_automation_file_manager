# File Organizer

## Overview
This Python script organizes files from one or more source folders into categorized subfolders in a specified destination directory. The categories include Images, Documents, Videos, Music, Compressed files, Programs, and Others. It also provides a desktop notification upon completion.

## Features
- Automatically organizes files based on their types (e.g., `.jpg` to Images, `.pdf` to Documents).
- Supports multiple source folders.
- Creates categorized subfolders in the destination directory.
- Sends a desktop notification after completing the organization process.
- Skips directories and processes only files.
- Handles missing source folders gracefully.

## Requirements
- Python 3.6 or higher
- `plyer` library for desktop notifications

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/harith-abeysinghe/python_automation_file_manager.git
   cd python_automation_file_manager
   ```

2. Install dependencies:
   ```bash
   pip install plyer
   ```

## Usage
1. Edit the script to define the source folders and destination folder.
   ```python
   source_folders = [
       os.path.expanduser("~/Downloads"),  # Default Downloads folder
       # Add more source folders as needed
   ]
   destination_folder = "D:\\From Downloads"
   ```

2. Run the script:
   ```bash
   python main.py
   ```

3. The script will process files from all valid source folders and organize them into the specified destination directory.

## Example
### Input:
- Source folder: `~/Downloads`
- Destination folder: `D:\From Downloads`

### Output:
The destination folder will have the following structure:
```
From Downloads/
├── Images/
├── Documents/
├── Videos/
├── Music/
├── Compressed/
├── Programs/
└── Others/
```

## Notifications
Once the file organization is complete, a desktop notification will display:
```
Title: File Organization Complete
Message: Files from all source folders have been organized into D:\From Downloads.
```

## Notes
- The script skips directories and processes only files.
- If a source folder does not exist, the script will print a warning and skip that folder.

Happy organizing! 🎉

