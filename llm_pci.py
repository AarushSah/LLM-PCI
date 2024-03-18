import os
import mimetypes

def process_folder(folder_path, output_file, level=0):
    """
    Recursively processes a folder and its contents, writing the structure and file contents to the output file.

    Args:
        folder_path (str): The path to the folder to process.
        output_file (TextIOWrapper): The file object to write the output to.
        level (int): The indentation level for the current folder (default is 0).
    """
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            process_file(item_path, output_file, level)
        elif os.path.isdir(item_path):
            include_folder = input(f"Include folder '{item}'? (y/n): ")
            if include_folder.lower() == 'y':
                output_file.write("  " * level + f"[Folder: {item}]\n")
                process_folder(item_path, output_file, level + 1)
            else:
                output_file.write("  " * level + f"[Skipped Folder: {item}]\n")

def process_file(file_path, output_file, level):
    """
    Processes a file and writes its contents to the output file based on the file type.

    Args:
        file_path (str): The path to the file to process.
        output_file (TextIOWrapper): The file object to write the output to.
        level (int): The indentation level for the current file.
    """
    _, extension = os.path.splitext(file_path)
    try:

        mime_type, _ = mimetypes.guess_type(file_path)
        if mime_type and mime_type.startswith("text/"):
            with open(file_path, "r") as file:
                content = file.read()
                output_file.write("  " * level + f"[File: {os.path.basename(file_path)}]\n")
                output_file.write("  " * (level + 1) + "```\n")
                output_file.write(content + "\n")
                output_file.write("  " * (level + 1) + "```\n")
            output_file.write("  " * (level + 1) + f"[File Type: {extension[1:].upper()}]\n")
        else:
            output_file.write("  " * level + f"[File: {os.path.basename(file_path)}]\n")
            output_file.write("  " * (level + 1) + f"[File Type: {extension[1:].upper()}]\n")
            output_file.write("  " * (level + 1) + f"[File Size: {os.path.getsize(file_path)} bytes]\n")
    except Exception as e:
        print("\033[93m" + f"Error processing file '{file_path}': {e} \n\n Continuing..." + "\033[0m")
        output_file.write("  " * level + f"[File: {os.path.basename(file_path)}]\n")
        output_file.write("  " * (level + 1) + f"[File Type: {extension[1:].upper()}]\n")
        output_file.write("  " * (level + 1) + f"[File Size: {os.path.getsize(file_path)} bytes]\n")
        output_file.write("  " * (level + 1) + f"[File could not be read]\n")

# Specify the folder path and output file name
folder_path = "C:/Users/aarus/Desktop/rowena-chat-demo"
output_file_name = "project_context.txt"

# Open the output file in write mode
with open(output_file_name, "w") as output_file:
    output_file.write(f"Project Context for: {folder_path}\n\n")
    # Start processing the folder
    process_folder(folder_path, output_file)

print(f"Project context has been written to: {output_file_name}")