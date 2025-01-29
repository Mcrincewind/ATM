import pyodbc
import analipsi
def efmanish_hristwn():
    
    connections_string=(
    'Driver={ODBC Driver 17 for SQL Server};'
    'Server=TE1-13\\SQLEXPRESS01;'
    'Database=ATM;'
    'Trusted_Connection=yes;'
    )

    try:
        conn=pyodbc.connect(connections_string)
        print("Connected to the database succesfully!")

        cursor=conn.cursor()
    
        cursor.execute("select * from dbo.Users")
        rows=cursor.fetchall()

        for row in rows:
            print(row)
    except Exception as e:
        print("ERROR  connection to the database:",e)
    finally:
        print('exit')
    if conn:
        conn.close()

efmanish_hristwn()






