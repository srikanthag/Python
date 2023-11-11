"""bridge pattern"""
"""composition is has a reletionship and inheritence is a relationship"""
import csv
class Consollogger:
    def log(self, message):
        print(message)

class Textfilelog:
    def __init__(self, file):
        self.file = file

    def log(self, message):
        self.file.write(message)
        self.file.write("\n")
        self.file.flush()

class CSVfileloger:
    def __init__(self, file):
        self.file = file

    def log(self, message):
        csv_writer = csv.writer(self.file)
        parts = message.split()


# f = open('_test.txt', 'w')
# print(f)
# l = Textfilelog(f)
# print(l.log('hello world'))
# print(l.log('hello universe'))

# f = open('_test.CSV', 'w')
# print(f)
# l = CSVfileloger(f)
# print(l.log('hello world'))
# print(l.log('hello universe'))







