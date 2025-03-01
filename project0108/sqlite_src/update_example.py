import sqlite3
from datetime import datetime

# connect to SQLite database
connection = sqlite3.connect("customer_order.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

def update_customer_by_order(customer_id, new_order_id):
    # connect to SQLite database
    connection = sqlite3.connect("customers_master")
    cursor = connection.cursor()
    query = "UPDATE orders SET order_id = ? WHERE customer_id = ?;"
    cursor.execute(query,(new_order_id, customer_id))

    # Commit changes
    connection.commit()

    # check if the update was successful
    if cursor.rowcount > 0:
        print(f'row count = {cursor.rowcount}' -- Updated rows. customer_id {customer_id}'s ')






def get_customer_by_order(order_id):
    # Dynamic SELECT query using a parameterized query
    query = "SELECT c.customer_id, first_name, last_name from orders as o, customers_master as c, product_master as p WHERE o.customer_id = c.customer_id and o.product_id = p.product_id and o.order_id= ? group by o.customer_id, first_name and last_name;"
    cursor= connection.cursor()
    cursor.execute(query, (order_id,))

        # Fetch and print results
    customers = cursor.fetchall()
    if customers:
        print(f"Customers in Order {order_id}:")
        for x in customers:
            print(f"ID: {x['customer_id']} {x['first_name']} {x['last_name']}")
    else:
        print(f"No customer found in Order List {order_id}.")

order_id = input("Enter Order ID: ")
get_customer_by_order(order_id)
    


    
    