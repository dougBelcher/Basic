# Use pandas to extract data from Excel and write to SQL text file
# Steps to take prior to running script
#   1)  Name column over Serial Numbers "Serial_Numbers"
#   2)  Make sure all the separation characters are the same in the file & script

import pandas as pd

Sensi = pd.read_excel('PICK 08867794(0).xlsx')

# Open the SQL text file
file1 = open("Sensi.sql", "w+")
a = 0

# Start writing SQL statements to file
file1.write('Select mdsn as "Serial Nbr"'
            ', mduser as "User", mdpid as "Pgm ID", mdjobn as "Job Nbr", date(char(1900000+mdupmj)) as "Date Upd"'
            ', mdpsn as "Pick", mditm as "Shrt Item", mdlitm as "Long Item"\n\tfrom wrddta/f5543203 a'
            '\n\twhere mdsn in (')

Sensi['SN'] = Sensi.Serial_Numbers.astype("string").str.split(pat="-")

for serial in Sensi.SN:
    if a == 0:
        a = 1
    else:
        file1.write(", ")
    for nbr in serial:
        file1.write("\'" + nbr.upper() + "\'")
        file1.write(", ")
    a = 0
    file1.write("\n\t")

file1.write("\'\')")

file1.write("\n\tand not exists(select 1 from wrddta/f5842007 b where a.mdsn=b.assn)")
file1.write("\n\tand mdsn<>' '")

file1.close()