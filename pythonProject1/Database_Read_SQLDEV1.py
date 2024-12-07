import cx_Oracle
import subprocess

# Oracle database connection details
username = 'sys'
password = 'admin'
host = 'localhost'
port = '1521'
service_name = 'XE'

# Create the connection string
dsn = cx_Oracle.makedsn(host, port, service_name=service_name)

# Establish the connection as SYSDBA
connection = cx_Oracle.connect(user=username, password=password, dsn=dsn, mode=cx_Oracle.SYSDBA)

# Create a cursor object
cursor = connection.cursor()

# Execute a SQL query to fetch data from the employee table
cursor.execute("SELECT * FROM employee")

# Fetch all rows from the query result
rows = cursor.fetchall()

# Print the rows
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
