import pandas as pd
from tabulate import tabulate
import os
import glob


file_path = ""
column_email = ""
column_name = ""
column_country = ""
column_zip = ""
column_phone = ""
column_item_title = ""  

desired_keyword = ""

csv_files = glob.glob(os.path.join(file_path, '*.csv'))

for csv_file in csv_files:
    
    data = pd.read_csv(csv_file, header=1)

    
    data = data.dropna(subset=[column_item_title], how="any")

    
    filtered_data = data[data[column_item_title].str.contains(desired_keyword, case=False, na=False)]


    if not filtered_data.empty:
        email = filtered_data[column_email].tolist()
        name = filtered_data[column_name].tolist()
        country = filtered_data[column_country].tolist()
        Zip = filtered_data[column_zip].tolist()
        phone = filtered_data[column_phone].tolist()
        item_Title = filtered_data[column_item_title].tolist()

        table_data = list(zip(email, name, country, Zip, phone,item_Title ))

        header = ["Email", "Name", "Country", "Zip", "Phone", "item_Title"]

        table = tabulate(table_data, headers=header, tablefmt="plain")
        print(f"Файл: {csv_file}")
        print(f"Clients with 'item title', contains '{desired_keyword}':")
        print(table)
        print("-----")
    else:
        print(f"In the file  {csv_file} not have client with 'item title', contains '{desired_keyword}'")
