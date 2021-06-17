#   This script is intended to read a directory of .csv files and output a file on the IBM i
import os
import pandas as pd

os.chdir('\\Users\\WRA1523\\')
file1 = open("MACSensi.csv", "w+")
hdr_parm = True

os.chdir('//wrprod/wrdsup/supdata')
directory = os.path.join('//wrprod/wrdsup/supdata')
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".csv"):
            f = open(file, 'r')
            try:
                df = pd.read_csv(file)
                if df.size > 0:
                    if hdr_parm:
                        df["file_name"] = file
                        df.to_csv(file1, index=False, header=hdr_parm, line_terminator='\n')
                        hdr_parm = False
                    else:
                        df["file_name"] = file
                        df.to_csv(file1, index=False, header=hdr_parm, line_terminator='\n')
                else:
                    print(f"Empty Data File: {file}")
                f.close()
            except:
                print(f"Can't access file : {file}")

print('done')
file1.close()
