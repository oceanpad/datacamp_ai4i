from sqlalchemy import *

metadata = MetaData()

engine = create_engine('mysql+mysqlconnector://root:root@localhost/dsta_map')

for name in engine.table_names():
  print name

data = Table('data', metadata, autoload=True, autoload_with=engine)

for name in data.columns:
  print name

stmt = select([data]).where(data.columns.id > 0).limit(11)

connection = engine.connect()

result = connection.execute(stmt)
for row in result:
  print(len(row))
  print(row[0])
connection.close()
