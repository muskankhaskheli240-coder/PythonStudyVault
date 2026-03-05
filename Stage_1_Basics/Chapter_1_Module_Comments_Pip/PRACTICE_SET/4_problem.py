import os

# Specify the directory path
directory_path = "/"

try:
    # Get list of files and directories
    contents = os.listdir(directory_path)

    # Print each item 
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("Error: The specified directory does not exist.")
except PermissionError:
    print("Error: Permission denied to access this directory.")
