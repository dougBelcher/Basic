#   ibm i pgm to upload sensi info
import sqlalchemy as sa
from dotenv import DotEnv
import sys
import os

os.chdir('C:\\Users\\WRA1523\\Dropbox\\Yellow Folders\\Python')

dotenv = DotEnv()

print(f"{dotenv.has('ibm_profile')}")
sys.exit()

engine = sa.create_engine("ibmi://ibm_profile:ibm_password@WRSERV/rdbname[S785b980]")

cnxn = engine.connect()
metadata = sa.MetaData()
table = sa.Table('BU100', metadata, autoload=True, autoload_with=engine)

query = sa.select([table])

result = cnxn.execute(query)
result = result.fetchall()

# print first entry
print(result[0])