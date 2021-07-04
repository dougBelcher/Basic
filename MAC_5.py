import sqlite3

conn = sqlite3.connect('TestDB.db')

c = conn.cursor()

# Create table - MAC

try:
    c.execute("""CREATE TABLE MAC( 
                MACaddress text PRIMARYKEY, 
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

many_customers = [('346F92000533', '8642WF04X00134', '01/24/2014', '01/24/2014', 'file'),
                  ('346F92000534', '8642WF04X00135', '01/24/2014', '01/24/2014', 'file'),
                  ('346F92000535', '8642WF04X00125', '01/24/2014', '01/24/2014', 'file'),
                  ('346F92000536', '8642WF04X00131', '01/24/2014', '01/24/2014', 'file')]

c.executemany("INSERT INTO MAC VALUES(?,?,?,?,?)", many_customers)

conn.commit()

# Query the Database

c.execute("SELECT * FROM MAC")

item = c.fetchall()
for items in item:
    print(f'{items}')

print(f'\nCommand executed successfully')

# Commit our command
conn.commit()

# Close our connection
conn.close()
