import sqlite3
from datetime import datetime

# connect to SQLite database
connection = sqlite3.connect("customer_order.db")

# drop table
connection.execute ("DROP TABLE product_master")
# create table
connection.execute("""
CREATE TABLE if NOT EXISTS product_master(
			Product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            Product_name VARCHAR(15) NULL,
            Nature VARCHAR(25) NULL,
            Model VARCHAR(25) NULL,
            Country VARCHAR(25) NULL,
            Brand VARCHAR(20) NULL
        	);
""")
cursor = connection.cursor()

# Insert data with current datetime
# event_name = "Python Workshop"
# event_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Format datetime as text
cursor.execute("INSERT INTO product_master(Product_id, Product_name, Nature, Model, Country, Brand) VALUES(?,?,?,?,?,?)",('1','iphone 16', 'phone', 'IHSVD', 'China', 'Apple'))
cursor.execute("INSERT INTO product_master(Product_id, Product_name, Nature, Model, Country, Brand) VALUES(?,?,?,?,?,?)",('2','SamsungS24', 'phone', 'hdvja','China','Samsung'))
							
 
# Commit changes
connection.commit()

# Retrieve data
cursor.execute("SELECT * FROM product_master;")
product_master = cursor.fetchall()
print("Events after insertions:", product_master)

connection.close()