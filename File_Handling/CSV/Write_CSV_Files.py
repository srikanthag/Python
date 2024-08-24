import csv

with open("example.csv", "w") as csv_file:
    write_obj = csv.writer(csv_file)
    write_obj.writerow(["x", "y", "z"])
    write_obj.writerow([10, 20, 30])
    write_obj.writerows([(1,2,3), (5,6,7), (8,9,7)])


with open("example.csv", "w") as csv_file:
    dictwriter_obj = csv.DictWriter(csv_file,["x","y","z"])
    dictwriter_obj.writeheader()
    dictwriter_obj.writerow({"x": 10,"y":20,"z":30 })

