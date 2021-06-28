#   This script is intended to read a directory of .csv files and output a file to SQLite
import os
import sys
import pandas as pd
from dotenv import DotEnv
import sqlite3

os.chdir('C:\\Users\\WRA1523\\Dropbox\\Yellow Folders\\Python')           # work
# os.chdir('C:\\Users\\Doug\\Documents\\Dropbox\\Yellow Folders\\Python')   # home PC
# os.chdir('/home/doug/Dropbox/Yellow Folders/Python')                        # ubuntu

dotenv = DotEnv()

os.chdir('\\Users\\WRA1523\\')                                              # work
# os.chdir('/home/doug/Dropbox/Doug')                                         # ubuntu
# os.chdir('C:\\Users\\Doug\\Documents')                                      # home PC

conn = sqlite3.connect('MAC_data.db')
c = conn.cursor()

c.execute("""CREATE TABLE MAC (
        MAC_ID text,
        SN text,
        F_name text
        )""")

sys.exit()

# os.chdir('//wrprod/wrdsup/supdata')                                         # work
# os.chdir('//wrprod/wrdsup/supdata')                                         # ubuntu
# os.chdir('//wrprod/wrdsup/supdata')                                         # home PC

directory = os.path.join('//wrprod/wrdsup/supdata')
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".csv"):
            f = open(file, 'r')
            try:
                df = pd.read_csv(file)
                if df.size > 0:
                    # if hdr_parm:
                    #     df["file_name"] = file
                    #     df.to_csv(file1, index=False, header=hdr_parm, line_terminator='\n')
                    #     hdr_parm = False
                    # else:
                    #     df["file_name"] = file
                    #     df.to_csv(file1, index=False, header=hdr_parm, line_terminator='\n')
                    pass
                else:
                    print(f"Empty Data File: {file}")
                f.close()
            except:
                print(f"Can't access file : {file}")

print('done')
file1.close()