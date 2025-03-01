import sqlite3
from datetime import datetime

# connect to SQLite database
connection = sqlite3.connect("example.db")

# create table
connection.execute("""
CREATE TABLE if NOT EXISTS events(
    event_id INTEGER PRIMARY KEY,
    name varchar(50) NOT NULL,
    event_date DATETIME NOT NULL
);
""")

cursor = connection.cursor()

# Insert data with current datetime
event_name = "Python Workshop"
event_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Format datetime as text
cursor.execute("INSERT INTO events (name, event_date) VALUES (?, ?)", (event_name, event_date))

# Commit changes
connection.commit()

# Retrieve data
cursor.execute("SELECT * FROM events;")
events = cursor.fetchall()
print("Events after insertions:", events)

connection.close()