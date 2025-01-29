import pyodbc;


connection_string=(
'Driver={ODBC Driver 17 for SQL Server};'
'Server=TE1-14\\SQLEXPRESS01;'
'Database=TEST;'
'Trusted_Connection=yes;')


try:
    conn= pyodbc.connect(connection_string)
    print("Connected to the database successfully!")
    cursor=conn.cursor()

    cursor.execute("INSERT INTO dbo.Boats (bid, bname, color) VALUES (200, 'Delulu', 'purple')")
    conn.commit()
    cursor.execute("SELECT * FROM dbo.Boats")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
 
except Exception as e:
 print("Error connecting to the database:",e)

