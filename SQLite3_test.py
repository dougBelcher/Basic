# SQLite Databases with Python

import sqlite3

conn = sqlite3.connect('customer.db')

# conn = sqlite3.connect(':memory:')  don't save the db

# Create a cursor
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE customers (
        first_name text,
        last_name text,
        email text
        )""")

# Commit our command
conn.commit()

# Close our connection
conn.close()