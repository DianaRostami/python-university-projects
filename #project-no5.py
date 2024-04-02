#count and rename the files in a folder
#os is a built-in module with methods for interacting with the operating system

import os

# Get the directory path from the user
folder_path = input("Please enter the directory path: ")

# Count the number of files
# os.listdir = Returns a list of the names of the entries in a directory
file_count = len(os.listdir(folder_path))
print("Number of files in the directory: {file_count}")

# Edit the names 
for filename in os.listdir(folder_path):
    if filename.endswith((".jpg", ".png",".txt")):
        new_filename = os.path.splitext(filename)[0] + "_edit" + os.path.splitext(filename)[1]
        print(f"{filename} => {new_filename}")