import pandas as pd

from sqlalchemy import create_engine

mysql_engine = create_engine('mysql+pymysql://root:Omnitech%407329@localhost:3306/student')

df_mysql = pd.read_sql("select * from employees", mysql_engine)
# print(df_mysql)
oracle_engine = create_engine('oracle+cx_oracle://system:admin@localhost:1521/?service_name=XE&mode=SYSDBA')

myOracle_engine = oracle_engine.connect()

df_oracle = pd.read_sql("select * from employee", myOracle_engine)

# print(df_oracle)
df_result = pd.merge( df_oracle,df_mysql, left_on='emp_no', right_on='id', how='outer')

print(df_result)

