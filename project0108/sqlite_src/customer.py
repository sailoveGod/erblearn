import sqlite3
from datetime import datetime

# connect to SQLite database
connection = sqlite3.connect("customer_order.db")

# drop table
#connection.execute ("DROP TABLE customers_master")
# create table
connection.execute("""
CREATE TABLE if NOT EXISTS customers_master(
			Customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name varchar(500) not null,
            last_name varchar(500) not null,
            DOB date not null,
            gender varchar(6) not null
        	);
""")
#DOB date not null
cursor = connection.cursor()

# Insert data with current datetime
# event_name = "Python Workshop"
# event_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Format datetime as text
cursor.execute("INSERT INTO customers_master (Customer_id, first_name, last_name, DOB, gender) VALUES(?,?,?,?,?)",('1', 'Donald', 'Wan', '1998/2/21','Male'))
cursor.execute("INSERT INTO customers_master (Customer_id, first_name, last_name, DOB, gender) VALUES(?,?,?,?,?)",('2', 'Winnie', 'Chan', '1994/8/24','Female'))
							

# Commit changes
connection.commit()

# Retrieve data
cursor.execute("SELECT * FROM customers_master;")
customers_master = cursor.fetchall()
print("Events after insertions:", customers_master)

connection.close()