import os
file_path = "secondex.txt"
if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    else:
        print(f"Error: You do not have permission to delete the file '{file_path}'.")
else:
    print(f"Error: The file '{file_path}' does not exist.")