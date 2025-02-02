""" 1. File Object Attributes"""
# When you open a file using the built-in open() function, you can get certain attributes from the file object.

import os
# Opening a file in read mode
file = open(r'D:\IT\Python\OS_Module\Sample\sample.txt', 'r')

# Attributes of the file object
print("File name:", file.name)  # Name of the file
print("File mode:", file.mode)  # Mode in which the file was opened (e.g., 'r', 'w')
print("File closed:", file.closed)  # Whether the file is closed or not

# Closing the file
file.close()

# ----------------------------------------------------------------------------------------------------------------

""" 2. File System Attributes"""
# Python provides a module os that lets you get additional file attributes related to the file system, such as file size, creation time, and last modification time.

import os

file_stats = os.stat(r'D:\IT\Python\OS_Module\Sample\sample.txt')

# Get current directory
print (os.getcwd())

# File size in bytes
print("File size:", file_stats.st_size, "bytes")

# Last modification time
import time
print("Last modified:", time.ctime(file_stats.st_mtime))

# Creation time (on some systems like Windows)
print("Creation time:", time.ctime(file_stats.st_ctime))

# File path exist or not
print(os.path.exists(r"D:\IT\Python\OS_Module\Sample\sample.txt"))

# List of files
print(os.listdir(r"D:\IT\Python"))

# Create new Directory
print(os.mkdir('___python'))

# Removing directory
print(os.rmdir('___python'))

# ----------------------------------------------------------------------------------------------------------------

""" 3. Other Methods for File Attributes"""
import os

file_path = r"D:\IT\Python\OS_Module\Sample\sample.txt"

# Check if file exists
if os.path.exists(file_path):
    print(f"{file_path} exists.")
    if os.path.isfile(file_path):
        print(f"{file_path} is a file.")
    if os.path.getsize(file_path) > 0:
        print(f"{file_path} is not empty.")
else:
    print(f"{file_path} does not exist.")

# ----------------------------------------------------------------------------------------------------------------

""" 4. opening a file in both read and write mode """
with open(file_path, "r+") as file:
    print(file.readable())
    print(file.writable())
