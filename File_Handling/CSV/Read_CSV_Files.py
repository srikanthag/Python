import csv
path = r"C:\Users\hp\Desktop\IT\Python\Python\File_Handling\File_Directory\CSV_Samples\sample.csv"
with open(path) as csv_file:
    read_obj = csv.reader(csv_file)
    print(read_obj)
    for row in read_obj:
        print(row)

# using DictReader
with open(path) as csv_file:
    read_obj = csv.DictReader(csv_file)
    print(read_obj)                       # iterator object
    for row in read_obj:
        print(row)                        # read row as a list