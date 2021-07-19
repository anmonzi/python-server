import sqlite3
import json
from models import Customer

CUSTOMERS = [
    {
        "id": 1,
        "name": "Hannah White",
        "address": "7002 Chestnut Ct",
        "email": "hannah@hannahwhite.com",
        "animalId": 1
    },
    {
        "id": 2,
        "name": "Stacey Burns",
        "address": "5000 Liberty Way",
        "email": "stacy@stacyburns.com",
        "animalId": 3
    },
    {
        "id": 3,
        "name": "Mike Harding",
        "address": "Highway 70 South",
        "email": "mike@mikeharding.com",
        "animalId": 2
    },
    {
        "id": 4,
        "name": "Emily Dauer",
        "address": "5862 Dickerson Pike",
        "email": "emily@emilydauer.com",
        "animalId": 5
    },
    {
        "id": 5,
        "name": "Kyle Smith",
        "address": "55 South Street",
        "email": "kyle@kylesmith.com",
        "animalId": 4
    }
]

# Old function for CUSTOMERS list above
# def get_all_customers():
#     """Return a list of customers
#     Returns:
#         [List]: list of dictionaries
#     """
#     return CUSTOMERS



# SQL GET function
def get_all_customers():
    """Return a list of customers
    """
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:
        # Black box area
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the info you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        """)

        # Initialize an empty list to hold all customer representations
        customers = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:
            # Create a customer instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Customer class imported above.
            customer = Customer(row['id'], row['name'], row['address'],
                                row['email'], row['password'])

            customers.append(customer.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(customers) #converts Python object into a json string



# Old function for CUSTOMERS list above
# # Function with a single parameter
# def get_single_customer(id):
#     """Returns a single customer by Id
#     """
#     # Variable to hold the found customer, if it exists
#     requested_customer = None

#     # Iterate the EMPLOYEES list above. Similar to the
#     # for..of loops used in JavaScript.
#     for customer in CUSTOMERS:
#         # Dictionaires in Python use [] notation to find a key
#         # instead of the dot notation that JS used.
#         if customer["id"] == id:
#             requested_customer = customer

#     return requested_customer



# SQL GET function
def get_single_customer(id):
    """Return a single customer by Id"""
    with sqlite3.connect("./kennel.db") as conn:
        # Black box area
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create a customer instance from the current row
        customer = Customer(data['id'], data['name'], data['address'],
                            data['email'], data['password'])

        return json.dumps(customer.__dict__)





def create_customer(customer):
    """Create a NEW customer
    """
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]
    # Add 1 to whatever that number is
    new_id = max_id + 1
    # Add an `id` property to the customer dictionary
    customer["id"] = new_id
    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)
    # Return the dictionary with `id` property added
    return customer


def delete_customer(id):
    """Delete a customer by Id
    """
    # Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    # Iterate the CUSTOMERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop() to remove it from the list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)


def update_customer(id, new_customer):
    """Edit a customer by Id
    """
    # Iterate the CUSTOMERS list, but with enumerate() so that
    #  you can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Update the value.
            CUSTOMERS[index] = new_customer
            break
