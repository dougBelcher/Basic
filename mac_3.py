import os
import pandas as pd

os.chdir('\\Users\\WRA1523\\')
file1 = open("MACSensi.csv", "w+")
hdr_parm = False

os.chdir('//wrprod/wrdsup/supdata')
directory = os.path.join('//wrprod/wrdsup/supdata')
for root,dirs,files in os.walk(directory):
    for file in files:
       if file.endswith(".csv"):
           f = open(file, 'r')
           df = pd.read_csv(file)
           print(f'{file}')
           df["file_name"] = file
           df.to_csv(file1, index=False, header=True, line_terminator='\n')
           f.close()
