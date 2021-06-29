#   This script is intended to read a directory of .csv files and output a file to SQLite
import os
import sys
import pandas as pd
from dotenv import DotEnv
import sqlite3
from pprint import pprint

os.chdir('C:\\Users\\WRA1523\\Dropbox\\Yellow Folders\\Python')           # work
# os.chdir('C:\\Users\\Doug\\Documents\\Dropbox\\Yellow Folders\\Python')   # home PC
# os.chdir('/home/doug/Dropbox/Yellow Folders/Python')                        # ubuntu

dotenv = DotEnv()

os.chdir('\\Users\\WRA1523\\')                                              # work
# os.chdir('/home/doug/Dropbox/Doug')                                         # ubuntu
# os.chdir('C:\\Users\\Doug\\Documents')                                      # home PC

conn = sqlite3.connect('MAC_data.db')
c = conn.cursor()

try:
    c.execute("""CREATE TABLE MAC (
            MACADDRESS text,
            SERIALNUMBER text,
            DATECODE text,
            TESTDATE text,
            file_name text
            )""")
except:
    pass

# Delete Records
c.execute("""DELETE FROM MAC""")

conn.commit()

# Set up for many ID insert
# many_SN = [('346F921B4C04', '710482321278C6', '6/7/2021', '6/7/2021', '20210609123119292imics1.csv'),
#            ('346F921B4C0E', '710482321278D0', '6/7/2021', '6/7/2021', '20210609123119292imics1.csv'),
#            ('346F921B4C0F', '710482321278D1', '6/7/2021', '6/7/2021', '20210609123119292imics1.csv'),
#            ('346F921B4C14', '710482321278D6', '6/7/2021', '6/7/2021', '20210609123119292imics1.csv')]

# c.executemany("INSERT INTO MAC VALUES(?, ?, ?, ?, ?)", many_SN)

# Query the Database
# c.execute("SELECT rowid, * FROM MAC")

# pprint(f'{c.fetchall()}')

# sys.exit()

os.chdir('//wrprod/wrdsup/supdata')                                         # work
# os.chdir('//wrprod/wrdsup/supdata')                                         # ubuntu
# os.chdir('//wrprod/wrdsup/supdata')                                         # home PC

directory = os.path.join('//wrprod/wrdsup/supdata')
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".csv"):
            try:
                f = open(file, 'r')
                print(f'got this far: 1')
                df = pd.read_csv(file)
                print(f'got this far: 2')
                if df.size > 0:
                    print(f'got this far: 3')
                    # c.execute("INSERT INTO customers VALUES('John', 'Elder', 'john@codemy.com')")
                    df.to_sql(MAC, c, index=False, if_exists='append')
                else:
                    print(f"Empty Data File: {file}")
                f.close()
            except:
                print(f"Can't access file : {file}")

print('done')
file1.close()