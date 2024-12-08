import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:Omnitech%407329@localhost:3306/student')
connection = engine.connect()
query = 'select * from employees'
df_target = pd.read_sql(query, connection)
print (df_target)
df_source = pd.read_csv('employee.csv')
print (df_source)
df_result = df_source[~df_source['first_name'].isin(df_target['first_name'])]
print (df_result)
