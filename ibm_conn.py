#   Bare minimum
# import ibm_db_dbi as db2

# *LOCAL w/ myuser
# conn = db2.connect(user="dbelcher", password="d9d9b015^", database="S785B980")

# MyRDB w/ current user
conn = db2.connect(database="S785B980")

# Same as above, but using connection string
conn = db2.connect("DATABASE=*LOCAL;UID=myuser;PWD=Passw0rd")
conn = db2.connect("DATABASE=MyRDB")

print(f'{conn}')


# import pyodbc
#
# connection = pyodbc.connect(
#     driver='{iSeries Access ODBC Driver}',
#     system='10.49.194.152',
#     uid='dbelcher',
#     pwd='xxxxxxxx')
# c1 = connection.cursor()
#
# c1.execute('select * from qsys2.sysschemas')
# for row in c1:
#     print(row)
