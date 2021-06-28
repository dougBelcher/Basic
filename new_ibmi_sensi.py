""" Example program using IBM_DB against Db2"""
import os
import sys
import getpass
import platform
import ibm_db_dbi

# --------------------------------------------------
# Database Connection Settings
# --------------------------------------------------
database = "sample"
hostname = "modi"
userid = "db2inst1"
password = "mypasswd"
port = 50000

connect_string = "ATTACH=FALSE;"
# connect_string += "PROTOCOL=TCPIP;PORT=" + str(port) + ";"

connect_options = { "SQL_ATTR_INFO_PROGRAMNAME": "JHMTESTHELPERS", # 20 char max
                    "SQL_ATTR_INFO_USERID" : getpass.getuser(),    # 255 char max
                    "SQL_ATTR_INFO_WRKSTNNAME" : platform.node()   # 255 char max
                  }
# --------------------------------------------------
hdbi = None  # Connection Object
# --------------------------------------------------

try:
    hdbi = ibm_db_dbi.connect(connect_string,
        host=hostname, database=database,
        user=userid, password=password,
        conn_options=connect_options)
except ibm_db_dbi.Warning as warn:
    print("Connection warning:", warn)
except ibm_db_dbi.Error as err:
    print("connection error:", err)
    sys.exit(1)

if hdbi:
    print("connected")

# --------------------------------------------------
# Query 1
# --------------------------------------------------
print("\nQuery1 begin")

my_sql = """select distinct tabschema, tabname
             from syscat.tables
            where tabschema = 'DB2INST1';
"""

my_cursor = hdbi.cursor()

try:
    my_cursor.execute(my_sql)
except Exception as err:
    print("Error on Execute", err)

try:
    my_tables = my_cursor.fetchall()
except Exception as err:
    print("Error on Fetch", err)

for (tabschema,tablename) in my_tables:
    print(tabschema,tablename)

# --------------------------------------------------
# Query 2
# --------------------------------------------------
print("\nQuery2 begin")

my_sql = """select distinct tabschema, tabname
             from syscat.tables
            where tabschema = ?
              and type = ?;
"""

my_params = ("DB2INST1", "T")
my_cursor.execute(my_sql, my_params)

print("Cursor column descriptions")
for column_variable in my_cursor.description:
    print(column_variable)

column_name1 = my_cursor.description[0][0]
column_name2 = my_cursor.description[1][0]

my_tables = my_cursor.fetchall()

if my_tables:
    print("\n")
    print(column_name1, column_name2)
    for (tabschema,tablename) in my_tables:
        print(tabschema,tablename)

if my_cursor:
    my_cursor.close()

# --------------------------------------------------
# Clean up
# --------------------------------------------------
if hdbi:
    if hdbi.close():
        print("disconnected")

print("done")