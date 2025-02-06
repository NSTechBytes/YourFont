import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

def get_files_in_folder(folder_path):
    """
    Get a set of file names (without paths) in the given folder.
    """
    return set(os.path.basename(f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)))

def compare_folders(folder1, folder2):
    """
    Compare files between two folders and print differences.
    """
    # Get sets of files from both folders
    files_in_folder1 = get_files_in_folder(folder1)
    files_in_folder2 = get_files_in_folder(folder2)

    # Find files that are in folder1 but not in folder2
    files_only_in_folder1 = files_in_folder1 - files_in_folder2

    # Find files that are in folder2 but not in folder1
    files_only_in_folder2 = files_in_folder2 - files_in_folder1

    # Print results
    if files_only_in_folder1:
        print(f"\nFiles found in '{folder1}' but not in '{folder2}':")
        for file in sorted(files_only_in_folder1):
            print(f"  - {file}")
    else:
        print(f"\nAll files in '{folder1}' are also present in '{folder2}'.")

    if files_only_in_folder2:
        print(f"\nFiles found in '{folder2}' but not in '{folder1}':")
        for file in sorted(files_only_in_folder2):
            print(f"  - {file}")
    else:
        print(f"\nAll files in '{folder2}' are also present in '{folder1}'.")

def main():
    # Hide the root tkinter window
    Tk().withdraw()

    # Ask user to select the first folder
    print("Please select the first folder:")
    folder1 = askdirectory(title="Select First Folder")
    if not folder1:
        print("No first folder selected. Exiting.")
        return

    # Ask user to select the second folder
    print("\nPlease select the second folder:")
    folder2 = askdirectory(title="Select Second Folder")
    if not folder2:
        print("No second folder selected. Exiting.")
        return

    # Compare the two folders
    print(f"\nComparing files between:\n  Folder 1: {folder1}\n  Folder 2: {folder2}")
    compare_folders(folder1, folder2)

if __name__ == "__main__":
    main()