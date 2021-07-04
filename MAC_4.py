#   This script is intended to read a directory of .csv files and output a file to SQLite
import os
import sys
import pandas as pd
# from dotenv import DotEnv
import sqlite3
from pprint import pprint

# os.chdir('C:\\Users\\WRA1523\\Dropbox\\Yellow Folders\\Python')           # work
# os.chdir('C:\\Users\\Doug\\Documents\\Dropbox\\Yellow Folders\\Python')   # home PC
os.chdir('/home/doug/Dropbox/Yellow Folders/Python')                        # ubuntu

# dotenv = DotEnv()

# os.chdir('\\Users\\WRA1523\\')                                              # work
# os.chdir('/home/doug/Dropbox/Doug')                                         # ubuntu
# os.chdir('C:\\Users\\Doug\\Documents')                                      # home PC

conn = sqlite3.connect('MAC_data.db')
c = conn.cursor()

try:
    c.execute("""CREATE TABLE MAC (
            MACaddress text,
            SerialNumber text,
            BuildDate text,
            TestDate text,
            file_name text
            )""")
except:
    pass

# Delete Records
c.execute("""DELETE FROM MAC""")

conn.commit()

# os.chdir('//wrprod/wrdsup/supdata')                                         # work
# os.chdir('//wrprod/wrdsup/supdata')                                         # ubuntu
# os.chdir('//wrprod/wrdsup/supdata')                                         # home PC

# directory = os.path.join('//wrprod/wrdsup/supdata')                          # work
directory = os.path.join('/home/doug/Dropbox/Yellow Folders/Python/WR')        # ubuntu
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".csv"):
            try:
                f = open(file, 'r')
                df = pd.read_csv(file)
                if df.size > 0:
                    # c.execute("INSERT INTO customers VALUES('John', 'Elder', 'john@codemy.com')")
                    # print(f'{df.head()}')
                    df.to_sql('MAC', c, index=False, if_exists='append', method='multi')
                else:
                    print(f"Empty Data File: {file}")
                f.close()
            except ValueError:
                print(f'{df.head}')
            except:
                print(f"Can't access file : {file}")
                # Query the Database
                c.execute("SELECT * FROM MAC")

                item = c.fetchall()
                for items in item:
                    print(f'{items}')


# Query the Database
# c.execute("SELECT rowid, * FROM MAC")

# pprint(f'{c.fetchall()}')

# sys.exit()
print('done')
# file1.close
