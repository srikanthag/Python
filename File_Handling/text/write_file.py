#create a file
path = r"C:\Users\srikanth\Desktop\IT\Python\python_practice\python_class\file_directory\txt_log_files\\"
# with open (path + "file1.txt", "w") as file:
#     print(file)

#write file
# with open (path + "file1.txt", "a") as file:
#     file.writelines(["hi\n how\n are hi"])


#wap to copy the contet of sample.txt in to different file
# with open(r"C:\Users\srikanth\Desktop\IT\Python\python_practice\python_class\File_Directory\txt_log_files\sample.txt", "r") as file_read:
#     with open(r"C:\Users\srikanth\Desktop\IT\Python\python_practice\python_class\File_Directory\txt_log_files\file1.txt", "w") as file_write:
#         for line in file_read:
#             file_write.write(line)

with open(r"C:\Users\srikanth\Desktop\sample.txt", "w") as file:
    file.writelines(['hi how are you'])



