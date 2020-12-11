# Use pandas to extract data from Excel and write to SQL text file for VLITRACE
import pandas as pd

df = pd.read_excel('Derby Orders - 2020.10.19(0).xlsx')

# Open the SQL text file
file1 = open("WR - VLITRACE.sql", "w+")

# Start writing SQL statements to file
file1.write("Select *\n\tfrom shp4dta/vlitrace"
            "\n\twhere trordr in (")


trordr = ','.join([f"'0{n}'" for n in df.SDPSN])
# print(f"SELECT * from shp4dta/vlitrace where trordr in ({trordr})")
file1.write(trordr)

file1.write(")")

file1.close()
