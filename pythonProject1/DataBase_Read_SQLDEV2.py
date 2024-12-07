from sqlalchemy import create_engine
import pandas as pd

# Create the engine using Oracle connection string
engine = create_engine('oracle+cx_oracle://system:admin@localhost:1521/?service_name=XE&mode=SYSDBA')

# Establish the connection
connection = engine.connect()

# Define your query
query = 'SELECT * FROM employee'

# Execute the query and fetch the data into a pandas DataFrame
df = pd.read_sql(query, connection)

# Print the DataFrame
print(df)

# Don't forget to close the connection when you're done
connection.close()
