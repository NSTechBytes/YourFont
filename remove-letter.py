import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

def remove_dash_one_from_files(folder_path):
    # Iterate through all files in the selected folder
    for filename in os.listdir(folder_path):
        # Split the file name and extension
        name, ext = os.path.splitext(filename)
        
        # Check if the file name ends with '-1'
        if name.endswith('-1'):
            # Construct the new file name by removing '-1'
            new_name = name[:-2] + ext  # Remove the last two characters ('-1')
            
            # Full paths for old and new file names
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_name)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_name}")

def main():
    # Hide the root tkinter window
    Tk().withdraw()

    # Ask user to select the folder
    print("Please select the folder:")
    folder_path = askdirectory(title="Select Folder")
    if not folder_path:
        print("No folder selected. Exiting.")
        return

    # Remove '-1' from files in the selected folder
    remove_dash_one_from_files(folder_path)
    print("Files renamed successfully!")

if __name__ == "__main__":
    main()