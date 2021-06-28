#   This script is intended to read a directory of .csv files and output a file on the IBM i
#   Purpose is to accumulate a series of Sensi uploads from the supplier and output a MAC ID file

#   TODO - Add SQLite output to this
import os
import pandas as pd
from datetime import datetime

print (f'start: {datetime.now()}')
os.chdir('\\Users\\WRA1523\\')
MAC_file = open("MACSensi.csv", "w+")
hdr_parm = True

os.chdir('//wrprod/wrdsup/supdata')
directory = os.path.join('//wrprod/wrdsup/supdata')
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".csv"):
            try:
                f = open(file, 'r')
                df = pd.read_csv(file)
                if df.size > 0:
                    df["file_name"] = file
                    if hdr_parm:
                        df.to_csv(MAC_file, index=False, header=hdr_parm, line_terminator='\n')
                        hdr_parm = False
                    else:
                        df.to_csv(MAC_file, index=False, header=hdr_parm, line_terminator='\n')
                else:
                    print(f"Empty Data File: {file}")
                f.close()
            except PermissionError:
                print(f"Can't access file: {file}")
            except:
                print(f"Unknown error: {file}")

print(f'done: {datetime.now()}')
MAC_file.close()
