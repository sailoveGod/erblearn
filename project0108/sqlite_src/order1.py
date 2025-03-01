import sqlite3
from datetime import datetime

# connect to SQLite database
connection = sqlite3.connect("customer_order.db")
connection.execute("PRAGMA foregin_key = ON;")

# drop table
connection.execute ("DROP TABLE orders")
# create table
connection.execute("""
CREATE TABLE if NOT EXISTS orders(
			order_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            customer_id INTEGER, 
            product_id INTEGER, 
            unit_price Decimal(10,2), 
            order_qty int, 
            Amount Decimal(15,2), 
            order_date date, 
            Foreign Key (customer_id) References customers_master(customer_id),
            FOREIGN KEY (product_id) References product_master(product_id)
        	);
""")
#DOB date not null
cursor = connection.cursor()

# Insert data with current datetime
# event_name = "Python Workshop"
# event_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Format datetime as text
cursor.execute("INSERT INTO orders (order_id, customer_id, product_id, unit_price, order_qty, amount, order_date) VALUES(?,?,?,?,?,?,?)",('1','1','1','6000','1','orders.unit_price * orders.order_qty','2024-1-1'))

							

# Commit changes
connection.commit()

# Retrieve data
cursor.execute("SELECT * FROM orders;")
orders = cursor.fetchall()
print("Events after insertions:", orders)

connection.close()


# Delete From table.name
# where xxx > xxx
#       xxx = xxx