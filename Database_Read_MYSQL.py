import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:Omnitech%407329@localhost:3306/student')
connection = engine.connect()
query = 'select * from employees'
df = pd.read_sql(query, connection)
print(df)
