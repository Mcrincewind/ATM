import pyodbc

connections_string=(
    'Driver={ODBC Driver 17 for SQL Server};'
    'Server=TE1-13\\SQLEXPRESS01;'
    'Database=TEST;'
    'Trusted_Connection=yes;'
)
try:
    conn=pyodbc.connect(connections_string)
    print("Connected to the database succesfully!")

    cursor=conn.cursor()
    
    cursor.execute("select * from dbo.Boats")
    rows=cursor.fetchall()

    for row in rows:
        print(row)
except Exception as e:
    print("ERROR  connection to the database:",e)
finally:
    print('exit')
    if conn:
        conn.close()

try:
    conn=pyodbc.connect(connections_string)
    print("Connected to the database succesfully!")

    cursor=conn.cursor()
    cursor.execute("INSERT INTO dbo.Boats (bid, bname, color) VALUES (109, 'blacklion', 'red')")
    conn.commit()
    print("Data inserted successfully!")

    cursor.execute("DELETE FROM dbo.Boats WHERE bid='109'")
    conn.commit()
    print("Data inserted successfully!")

except Exception as e:
    print("ERROR  connection to the database:",e)
finally:
    print('exit')
    if conn:
        conn.close()