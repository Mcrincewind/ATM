import pyodbc
def deposit():
    try:
        # Ask the user for the account ID and deposit amount
        userID = int(input("Enter your account ID: "))
        deposit_amount = float(input("Enter the deposit amount: "))

        # Validate the deposit amount
        if deposit_amount <= 0:
            print("Deposit amount must be greater than 0.")
            return
        
        # Connect to the database
        connection_string = (
            'Driver={ODBC Driver 17 for SQL Server};'
            'Server=TE1-14\\SQLEXPRESS01;'  # Update with your server details
            'Database=ATM;'  # Database name
            'Trusted_Connection=yes;'  # Assuming Windows authentication
        )
        conn = pyodbc.connect(connection_string)
        print("Connected to the database successfully!")

        cursor = conn.cursor()

        # Check if the account exists
        cursor.execute("SELECT userMoney FROM accounts WHERE account_id = ?", (userID,))
        result = cursor.fetchone()

        if result is None:
            print(f"Account {userID} not found.")
            return

        userMoney = result[0]

        # Add the deposit amount to the current balance
        new_balance = userMoney + deposit_amount
        cursor.execute("UPDATE accounts SET userMoney = ? WHERE account_id = ?", (new_balance, userID))
        conn.commit()
        
        print(f"Deposit successful! New balance for account {userID}: ${new_balance:.2f}")

    except pyodbc.Error as e:
        print(f"Database error: {e}")
    except ValueError:
        print("Invalid input! Please enter numeric values for account ID and deposit amount.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the connection
        conn.close()

# Example usage
deposit()  # This will ask the user for account ID and deposit amount interactively