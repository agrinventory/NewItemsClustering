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

tables_to_fetch = ['dbo.items','dbo.item_detail','dbo.item_order_routes','dbo.mbe_item_standard','core.label','inv.item_label_link']

try:
    # Establish a connection
    conn = pyodbc.connect(connection_string)
    print("Connection successful!")

    # Define your SQL query
    sql_query = 'SELECT * FROM dbo.items'

    # Create a cursor object
    cursor = conn.cursor()

    # Execute the query
    cursor.execute(sql_query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Extract column names from the cursor description
    columns = [column[0] for column in cursor.description]

    # Create a list of dictionaries containing the data
    data = [dict(zip(columns, row)) for row in rows]

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    print(df.head(10))


except pyodbc.Error as ex:
    print("Connection failed: ", ex)

