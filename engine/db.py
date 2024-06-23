import sqlite3
conn = sqlite3.connect("jarvis2.db")
cursor = conn.cursor()

# Creating  the System Table
query = "CREATE TABLE IF NOT EXISTS sys_command3(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
#query = "INSERT INTO sys_command3 VALUES(null, 'one note', 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OneNote.exe')"
cursor.execute(query)
#conn.commit()

# Insert into the Web Table
query = "CREATE TABLE IF NOT EXISTS web_command4(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

#Insert into the Web table
query = "INSERT INTO web_command4 VALUES(null, 'whatsapp', 'https://web.whatsapp.com/')"
cursor.execute(query)
conn.commit()

import sqlite3


#def connect_to_db(db_name):
    #try:
        #con = sqlite3.connect(db_name)
        #cursor = con.cursor()
        #print("Connection established successfully")

        # Run a simple test query
       # cursor.execute("SELECT sqlite_version();")
        #result = cursor.fetchone()
        #print(f"SQLite version: {result[0]}")

        #return con, cursor
    #except sqlite3.Error as e:
        #print(f"Error connecting to database: {e}")
        #return None, None


# Example usage
#db_name = "jarvis2.db"
#con, cursor = connect_to_db(db_name)

#if con and cursor:
    # Continue with your database operations
    #print("Database operations can continue.")
#else:
    # Handle the connection failure
    #print("Database connection failed. Exiting.")



