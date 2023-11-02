import csv
path = r"C:\Users\hp\Desktop\IT\Python\Python\File_Directory\csv_files\employees.csv"
path2 = r"C:\Users\hp\Desktop\IT\Python\Python\File_Directory\csv_files\test.csv"
path3 = r"C:\Users\hp\Desktop\IT\Python\Python\File_Directory\csv_files\vaccination_data.csv"


#wap to read all the names of the employees in the employee.csv file
# with open(path) as csv_file:
#     emp = csv.reader(csv_file)
#     for row in emp:
#         print(row[0])

#wap to print only the salary that are >70000 their names
# with open(path) as csv_file:
#     emp = csv.reader(csv_file)
#     header = next(emp)
#     # print(header)
#     for row in emp:
#         if int(row[3]) > 70000:
#             print(row[0])

#wap to group male and female employee from group
# with open(path) as csv_file:
#     emp = csv.reader(csv_file)
#     header = next(emp)
#     # print(header)
#     d = {}
#     # d = {"male": [], "femele": []}
#     for row in emp:
#         if row[1] == "male":
#             d["male"] = [row[0]]
#         else:
#             d["female"] = [row[0]]
#     print(d)

#defalutdict
# from collections import defaultdict
# with open(path) as csv_file:
#     emp = csv.reader(csv_file)
#     header = next(emp)
#     dd = defaultdict(list)
#
#     for row in emp:
#         dd[row[1]] += [row[0]]
# print(dd)

#wap to group employees based on their team
# from collections import defaultdict
# with open(path) as csv_file:
#     emp = csv.reader(csv_file)
#     header = next(emp)
#     dd = defaultdict(list)
#
#     for row in emp:
#         dd[row[2]] += [row[0]]
# print(dd)

#normal
# with open(path) as csv_file:
#     emp = csv.reader(csv_file)
#     header = next(emp)
#     print(header)
#     d = {}
#     for row in emp:
#         if row[2] not in d:
#             d[row[2]] = [row[0]]
#         else:
#             d[row[2]] += [row[0]]
#     print(d)

#wap to sort the shares in test.csv file based on the share price
# with open(path2) as csv_file:
#     share = csv.DictReader(csv_file)
#     l = list(share)
#     res = sorted(l, key=lambda d: float(d["price"]))
#     print(list(res))

#wap add all the shares in test.csv file
# with open(path2) as csv_file:
#     share = csv.reader(csv_file)
#     next(share)
#     sum = 0
#     for amount in share:
#         sum += int(amount[1])
#     print(sum)

#analysing vaccination data
#total vaccination of all the countries
# with open(path3) as file:
#     vac = csv.reader(file)
#     header = next(vac)
#     print(header)
#     for row_ in vac:
#         print(row_[5])

#using dictreader
# with open(path3) as file:
#     vac = csv.DictReader(file)
#     header = next(vac)
#     print(header)
#     for row in vac:
#         print(row["TOTAL_VACCINATIONS"])



#total vaccination by country
# with open(path3) as file:
#     vac = csv.reader(file)
#     d = {}
#     for row in vac:
#         if row[0] not in d:
#             d[row[0]] = row[5]
#     print(d)


#names of countries and WHO region
# with open(path3) as file:
#     vac = csv.reader(file)
#     d = {}
#     for row in vac:
#         if row[0] not in d:
#             d[row[0]] = row[2]
#     print(d)


#country and persons vaccinated per 100 and top 3 contreies with most vaccinated countries
# from collections import Counter
# from collections import defaultdict
# with open(path3) as csv_file:
#     emp = csv.reader(csv_file)
#     header = next(emp)
#     dd = {}
#     for row in emp:
#         if row[7]:
#             dd[row[0]] = float(row[7])
#     # print(dd)
# res = sorted(dd.items(), key=lambda item: item[-1])
# print(res[-3:])


#countries with less than 10k vaccinated people
# with open(path3) as csv_file:
#     emp = csv.DictReader(csv_file)
#     header = next(emp)
#     print(header)
#     for row in emp:
#         total_vac = row["TOTAL_VACCINATIONS"]
#         if total_vac:
#             if int(total_vac) < 10000:
#                 print(row["COUNTRY"])


#get the latest updated country with its total vaccination and number people vaccinated
# from collections import defaultdict
# with open(path3) as csv_file:
#     emp = csv.DictReader(csv_file)
#     header = next(emp)
#     d = defaultdict(list)
#     for row in emp:
#         d[row["DATE_UPDATED"]] += [(row["COUNTRY"], row["TOTAL_VACCINATIONS"])]
#
# res = sorted(d.items())
# print(res[-1])







