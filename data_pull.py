import pandas as pd
import pyodbc as pyodbc


drivers = pyodbc.drivers()
print("Available ODBC Drivers:")
for driver in drivers:
    print(driver)

# Define your connection details
server = 'agressentials-mt.database.windows.net'
database = 'tenant_168'
username = 'agr-mt-admin'
password = 'Zmn3x28GtAQQxGbQ'

# Set up the connection string
connection_string = f'''
DRIVER={{SQL Server}};
SERVER={server};
DATABASE={database};
UID={username};
PWD={password};
Encrypt=false;
TrustServerCertificate=false;
Connection Timeout=30;
'''

print(connection_string)

# Establish a connection
conn = pyodbc.connect(connection_string)

# Create a cursor object
cursor = conn.cursor()

# Write an SQL query
sql_query = 'SELECT * FROM dbo.items'

# Execute the query
cursor.execute(sql_query)

# Fetch the data
rows = cursor.fetchall()

# Process and print the data
for row in rows:
    print(row)

# Close the connection
conn.close()
