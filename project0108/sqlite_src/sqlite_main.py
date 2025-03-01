import sqlite3
from datetime import datetime

# connect to SQLite database
connection = sqlite3.connect("customer_order.db")
connection.execute("PRAGMA foregin_key = ON;")

# drop table
connection.execute ("DROP TABLE customer")

# drop table
connection.execute ("DROP TABLE orders")