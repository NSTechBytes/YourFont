import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askdirectory

def move_files_ending_with_dash_one(source_folder, destination_folder):
    # Ensure the destination folder exists, if not create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate through all files in the source folder
    for filename in os.listdir(source_folder):
        # Check if the file ends with '-1' before the extension
        name, ext = os.path.splitext(filename)
        if name.endswith('-1'):
            # Construct full file path
            source_file_path = os.path.join(source_folder, filename)
            destination_file_path = os.path.join(destination_folder, filename)
            
            # Move the file to the destination folder
            shutil.move(source_file_path, destination_file_path)
            print(f"Moved: {filename}")

def main():
    # Hide the root tkinter window
    Tk().withdraw()

    # Ask user to select the source folder
    print("Please select the source folder:")
    source_folder = askdirectory(title="Select Source Folder")
    if not source_folder:
        print("No source folder selected. Exiting.")
        return

    # Ask user to select the destination folder
    print("Please select the destination folder:")
    destination_folder = askdirectory(title="Select Destination Folder")
    if not destination_folder:
        print("No destination folder selected. Exiting.")
        return

    # Move files ending with '-1'
    move_files_ending_with_dash_one(source_folder, destination_folder)
    print("Files moved successfully!")

if __name__ == "__main__":
    main()