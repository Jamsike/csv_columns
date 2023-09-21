# IMPORTANT - please download (pandas and tabulate) to code normally function.
# In general, the code works fine as it works - at the bottom indicated what to paste.
# It then enters the desired columns and if many files will be specified (Files go in sequence:)
# Also now all columns, and no value (Nan)

import pandas as pd
from tabulate import tabulate
import os
import glob

# In general, in file_path, specify here the path of the folder where you have csv files only without (*)!!!
file_path = ""
column_email = ""
column_name = ""
column_country = ""
column_zip = ""
column_phone = ""

csv_files = glob.glob(os.path.join(file_path, '*.csv'))

for csv_files in csv_files:
    # Loads column data:
    data = pd.read_csv(csv_files, header=1)

    # This extracts data from the column:
    email = data[column_email].tolist()
    name = data[column_name].tolist()
    country = data[column_country].tolist()
    Zip = data[column_zip].tolist()
    phone = data[column_phone].tolist()

    data = data.fillna(" ")

    table_data = list(zip(email,name,country,Zip,phone))

    header = ["Email", "Name", "Country", "Zip", "Phone"]

    table = tabulate(table_data, tablefmt="plain")
    print(f"Файлы идут по очередно: {csv_files}")
    print(data)
    print("----")

