import csv
path = r"C:\Users\srikanth\Desktop\IT\Python\Python\file_directory\csv_files\sample.CSV"
with open(path) as csv_file:
    read_obj = csv.reader(csv_file)
    print(read_obj)
    for row in read_obj:
        print(row)

# using DictReader
with open(path) as csv_file:
    read_obj = csv.DictReader(csv_file)
    print(read_obj)                       #itrerator object
    for row in read_obj:
        print(row)                         #reads row as a list

