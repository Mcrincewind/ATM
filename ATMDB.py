import pyodbc

# Set up the connection string
connection_db = (
    'Driver={ODBC Driver 17 for SQL Server};'
    'Server=TE1-12\SQLEXPRESS01;'  
    'Database=ATM;'
    'Trusted_Connection=yes;'
)

# Establish the connection
try:
    conn = pyodbc.connect(connection_db)
    print("Connected to the database successfully!")

    # Create a cursor to interact with the database
    cursor = conn.cursor()

    # Example: Execute a query
    cursor.execute("SELECT * FROM Users")  # Replace with your query
    rows = cursor.fetchall()

    # Process the results
    for row in rows:
        print(row)

except Exception as e:
    print("Error connecting to the database:", e)

finally:
    # Close the connection
    print('exit')
    if conn:
        conn.close()