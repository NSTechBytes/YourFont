import pyautogui
import time
import os
import shutil

def copy_icons_from_positions(positions, folder_pos, target_folder):
    for idx, (x, y) in enumerate(positions):
        # Move to the icon at the given (x, y) position
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.click()

        # Use keyboard shortcut to copy (Ctrl + C)
        pyautogui.hotkey('ctrl', 'c')

        # Wait for the copy action to complete
        time.sleep(0.5)

        # Move to the folder location
        pyautogui.moveTo(folder_pos[0], folder_pos[1], duration=0.5)
        pyautogui.click()

        # Check if the file already exists in the folder before pasting
        icon_filename = os.path.join(target_folder, f"icon_{idx + 1}.png")
        
        # If file exists, rename it to avoid conflict
        if os.path.exists(icon_filename):
            # Rename the file by appending a number
            counter = 1
            while os.path.exists(os.path.join(target_folder, f"icon_{idx + 1}_{counter}.png")):
                counter += 1
            icon_filename = os.path.join(target_folder, f"icon_{idx + 1}_{counter}.png")
        
        # Paste the icon (Ctrl + V) and save it
        pyautogui.hotkey('ctrl', 'v')

        # Wait for paste to complete
        time.sleep(1)

        # Rename the pasted file if needed
        # Use file operations to rename the file (works after paste)
        if os.path.exists(icon_filename):
            # If the file exists, rename it to the new one
            shutil.move(os.path.join(target_folder, "icon.png"), icon_filename)

        print(f"Icon {idx + 1} has been copied and saved as {icon_filename}")

# Example: A list of X, Y positions of icons (adjust based on your icons)
icon_positions = [
    # Row 1
    (215, 60), (263, 60), (313, 60), (372, 60), (423, 60), (480, 60), (537, 60), (592, 60), (645, 60), (696, 60), (753, 60), (802, 60), (858, 60), (912, 60),
    # Row 2
    (215, 119), (263, 119), (313, 119), (372, 119), (423, 119), (480, 119), (537, 119), (592, 119), (645, 119), (696, 119), (753, 119), (802, 119), (858, 119), (912, 119),
    # Row 3
    (215, 169), (263, 169), (313, 169), (372, 169), (423, 169), (480, 169), (537, 169), (592, 169), (645, 169), (696, 169), (753, 169), (802, 169), (858, 169), (912, 169),
    # Row 4
    (215, 218), (263, 218), (313, 218), (372, 218), (423, 218), (480, 218), (537, 218), (592, 218), (645, 218), (696, 218), (753, 218), (802, 218), (858, 218), (912, 218),
    # Row 5
    (215, 270), (263, 270), (313, 270), (372, 270), (423, 270), (480, 270), (537, 270), (592, 270), (645, 270), (696, 270), (753, 270), (802, 270), (858, 270), (912, 270),
    # Row 6
    (215, 323), (263, 323), (313, 323), (372, 323), (423, 323), (480, 323), (537, 323), (592, 323), (645, 323), (696, 323), (753, 323), (802, 323), (858, 323), (912, 323),
    # Row 7
    (215, 375), (263, 375), (313, 375), (372, 375), (423, 375), (480, 375), (537, 375), (592, 375), (645, 375), (696, 375), (753, 375), (802, 375), (858, 375), (912, 375),
    # Row 8
    (215, 426), (263, 426), (313, 426), (372, 426), (423, 426), (480, 426), (537, 426), (592, 426), (645, 426), (696, 426), (753, 426), (802, 426), (858, 426), (912, 426),
    # Row 9
    (215, 477), (263, 477), (313, 477), (372, 477), (423, 477), (480, 477), (537, 477), (592, 477), (645, 477), (696, 477), (753, 477), (802, 477), (858, 477), (912, 477),
    # Row 10
    (215, 532), (263, 532), (313, 532), (372, 532), (423, 532), (480, 532), (537, 532), (592, 532), (645, 532), (696, 532), (753, 532), (802, 532), (858, 532), (912, 532),
    # Row 11
    (215, 579), (263, 579), (313, 579), (372, 579), (423, 579), (480, 579), (537, 579), (592, 579), (645, 579), (696, 579), (753, 579), (802, 579), (858, 579), (912, 579),
    # Row 12
    (215, 626), (263, 626), (313, 626), (372, 626), (423, 626), (480, 626), (537, 626), (592, 626), (645, 626), (696, 626), (753, 626), (802, 626), (858, 626), (912, 626),
    # Row 13
    (215, 681), (263, 681), (313, 681), (372, 681), (423, 681), (480, 681), (537, 681), (592, 681), (645, 681), (696, 681), (753, 681), (802, 681), (858, 681), (912, 681),
    # Row 14
    (215, 732), (263, 732), (313, 732), (372, 732), (423, 732), (480, 732), (537, 732), (592, 732), (645, 732), (696, 732), (753, 732), (802, 732), (858, 732), (912, 732),
    # Row 15
    (215, 785), (263, 785), (313, 785), (372, 785), (423, 785), (480, 785), (537, 785), (592, 785), (645, 785), (696, 785), (753, 785), (802, 785), (858, 785), (912, 785),
    # Row 16
    (215, 836), (263, 836), (313, 836), (372, 836), (423, 836), (480, 836), (537, 836), (592, 836), (645, 836), (696, 836), (753, 836), (802, 836), (858, 836), (912, 836),
    # Row 17
    (215, 881), (263, 881), (313, 881), (372, 881), (423, 881), (480, 881), (537, 881), (592, 881), (645, 881), (696, 881), (753, 881), (802, 881), (858, 881), (912, 881),
    # Row 18
    (215, 941), (263, 941), (313, 941), (372, 941), (423, 941), (480, 941), (537, 941), (592, 941), (645, 941), (696, 941), (753, 941), (802, 941), (858, 941), (912, 941),
    # Row 19
    (215, 990), (263, 990), (313, 990), (372, 990), (423, 990), (480, 990), (537, 990), (592, 990), (645, 990), (696, 990), (753, 990), (802, 990), (858, 990), (912, 990),
]

folder_position = (1500, 500)  # Folder location (adjust for your screen setup)
target_folder = r"C:\Users\nstec\OneDrive\Desktop\Done"  # Folder where icons will be saved
# Allow some time to set up (e.g., open Pichon and your folder)
time.sleep(5)

# Start copying icons from the provided positions to the folder
copy_icons_from_positions(icon_positions, folder_position, target_folder)
