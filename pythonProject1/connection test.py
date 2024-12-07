from sqlalchemy import create_engine
import pandas as pd

# Oracle database connection details
username = 'sys'
password = 'admin'
host = 'localhost'
port = '1521'
service_name = 'XE'

# Create the Easy Connect string
connection_string = f'oracle+cx_oracle://{username}:{password}@{host}:{port}/{service_name} as sysdba'

# Create the SQLAlchemy engine
engine = create_engine(connection_string)

# Use pandas to read data from the employee table
query = 'SELECT * FROM employee'
df = pd.read_sql(query, con=engine)

# Print the dataframe
print(df)
