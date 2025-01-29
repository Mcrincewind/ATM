import pyodbc

def analipsi():
    try:
        
        EISODOS = input("Dwse to id: ")
        aferetiko_poso = float(input("Dwse to poso analipseis: "))

        
        connections_string = (
            'Driver={ODBC Driver 17 for SQL Server};'
            'Server=TE1-13\\SQLEXPRESS01;'
            'Database=ATM;'
            'Trusted_Connection=yes;'
        )

        conn = pyodbc.connect(connections_string)
        print("Connected to the database successfully!")

        cursor = conn.cursor()

        
        cursor.execute("SELECT userMoney FROM dbo.Users WHERE userID=?", (EISODOS,))
        row = cursor.fetchone()

        if row:
            ypoloipo = row[0]  
            print(f"Current balance: {ypoloipo}")

            
            if ypoloipo >= aferetiko_poso:
                ypoloipo -= aferetiko_poso
                print(f"New balance: {ypoloipo}")

                
                cursor.execute("UPDATE dbo.Users SET userMoney=? WHERE userID=?", (ypoloipo, EISODOS))
                conn.commit()
                print("Transaction successful! Balance updated.")
            else:
                print("Insufficient funds.")
        else:
            print("User not found.")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()
        print("Connection closed.")




