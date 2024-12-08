import pandas as pd
from sqlalchemy import create_engine
# Database connection details
db_type = 'mysql+pymysql'  # Replace with your database type and connector
username = 'root'
password = 'Omnitech%407329'
host = 'localhost'
database = 'student'

# Create a database connection
engine = create_engine(f'{db_type}://{username}:{password}@{host}/{database}')

# Function to check data types

def check_data_types(city):
    query = f"DESCRIBE {city}"
    df = pd.read_sql(query, con=engine)
    print(f"Data types for table '{city}':")
    print(df[['Field', 'Type']])
# Specify the table name
table_name = 'city'  # Replace with your table name
# Check data types
check_data_types(table_name)
