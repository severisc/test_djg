import sqlite3, json, sys
import pandas as pd

# connection to sqlite 
conn = sqlite3.connect('colibri_tst\\db.sqlite3')

c = conn.cursor()

# json file
raw = "raw_data\\MOCK_DATA.json"

with open(raw, "r") as f:
    data = json.load(f)   

df = pd.json_normalize(data)

df['industry'] = df['industry'].replace('n/a', None)

# df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], format='%d/%m/%Y')

# in pandas on a numeric column if there is a null value by default pandas will converts to double
# order to change data type from double to int have to replace null values with 0 
df['years_of_experience'] = df['years_of_experience'].fillna(0)
df['years_of_experience'] = df['years_of_experience'].astype("int")

# write to table employee
df.to_sql('app_1_employee', conn, if_exists='replace', index = False)