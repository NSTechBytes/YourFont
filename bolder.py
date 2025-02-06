import os
import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET

def make_svg_bolder(svg_file_path, output_folder, boldness=2):
    """
    Function to make an SVG file bolder by increasing its stroke-width.
    
    :param svg_file_path: Path to the original SVG file.
    :param output_folder: Folder where the modified SVG will be saved.
    :param boldness: Amount to increase stroke-width by (default is 2).
    """
    try:
        # Parse the SVG file
        tree = ET.parse(svg_file_path)
        root = tree.getroot()

        # Namespace dictionary for SVG elements
        namespaces = {'ns0': 'http://www.w3.org/2000/svg'}

        # Find all elements with a 'd' attribute (paths) and ensure they have stroke and stroke-width
        for element in root.findall(".//ns0:path", namespaces):
            # Add stroke if not present
            if 'stroke' not in element.attrib:
                element.set('stroke', 'black')  # Default stroke color
            
            # Get current stroke-width or set default if not present
            stroke_width = element.get('stroke-width')
            if stroke_width:
                try:
                    # Increase stroke width by the specified boldness
                    new_stroke_width = float(stroke_width) + boldness
                    element.set('stroke-width', str(new_stroke_width))
                except ValueError:
                    # If stroke-width isn't a number, set a default value
                    element.set('stroke-width', str(boldness))
            else:
                # If no stroke-width is defined, set a default value
                element.set('stroke-width', str(boldness))

        # Save the modified SVG file to the output folder
        file_name = os.path.basename(svg_file_path)
        output_path = os.path.join(output_folder, file_name)
        tree.write(output_path, encoding='utf-8', xml_declaration=True)

        print(f"Processed: {file_name}")

    except Exception as e:
        print(f"Error processing {svg_file_path}: {e}")


def process_svgs_in_folder(folder_path, boldness=2):
    """
    Function to process all SVG files in a folder and make them bolder.
    
    :param folder_path: Path to the folder containing SVG files.
    :param boldness: Amount to increase stroke-width by (default is 2).
    """
    # Create a subfolder to store modified SVGs
    output_folder = os.path.join(folder_path, "bolder_svgs")
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the selected folder
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith('.svg'):
            svg_file_path = os.path.join(folder_path, file_name)
            make_svg_bolder(svg_file_path, output_folder, boldness)

    print(f"All SVGs processed. Modified files are saved in: {output_folder}")


if __name__ == "__main__":
    # Initialize tkinter for folder selection
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window

    # Ask the user to select a folder
    folder_selected = filedialog.askdirectory(title="Select Folder Containing SVG Files")

    if folder_selected:
        print(f"Selected folder: {folder_selected}")
        
        # Use a fixed boldness value (default is 2)
        boldness = 2
        
        # Process all SVGs in the selected folder
        process_svgs_in_folder(folder_selected, boldness)
    else:
        print("No folder selected. Exiting.")