#   This script is intended to read a directory of .csv files and output a file on the IBM i
#   Purpose is to accumulate a series of Sensi uploads from the supplier and output a MAC ID file

#   TODO - Add SQLite output to this *edit* change to csvs-to-sqlite
import os
import sys
import pandas as pd
from datetime import datetime

print(f'start: {datetime.now()}')
# os.chdir('\\Users\\WRA1523\\')                    # work
os.chdir('/home/doug/Downloads')                    # ubuntu
# sys.exit()
MAC_file = open("MACSensi(0).csv", "w+")
hdr_parm = True

# os.chdir('//wrprod/wrdsup/supdata')                                           # work
# directory = os.path.join('//wrprod/wrdsup/supdata')                           # work
os.chdir('/home/doug/Dropbox/Yellow Folders/Python/WR')                        # ubuntu
directory = os.path.join('/home/doug/Dropbox/Yellow Folders/Python/WR')        # ubuntu
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".csv"):
            try:
                print('Step 1')
                f = open(file, 'r')
                print('Step 2')
                # print(f'{directory}')
                df = pd.read_csv(file)
                print('Step 3')
                if df.size > 0:
                    # df["file_name"] = file
                    print(f'Step 4: {file}')
                    if hdr_parm:
                        df.to_csv(MAC_file, index=False, header=hdr_parm, line_terminator='\n',
                                  columns='MACaddress, SerialNumber, BuildDate, TestDate, file_name')
                        hdr_parm = False
                    else:
                        df.to_csv(MAC_file, index=False, header=hdr_parm, line_terminator='\n',
                                  columns='MACaddress, SerialNumber, BuildDate, TestDate, file_name')
                else:
                    print(f"Empty Data File: {file}")
                f.close()
            except PermissionError:
                print(f"Can't access file: {file}")
            except Exception as e:
                print(f"Unknown error: {file} : {e}")

print(f'done: {datetime.now()}')
MAC_file.close()

