"Pandad"

# Pandas is defined as an open-source library which is built on the top of the NumPy library. It provides fast analysis, data cleaning,
# and preparation of the data for the user and supports both xls and xlsx extensions from the URL.

import pandas as pd

# Read the file
data = pd.read_csv(r"/File_Handling/EXCEL/student.xlsx")

# Output the number of rows
print("Total rows: {0}".format(len(data)))

# See which headers are available
print(list(data))
