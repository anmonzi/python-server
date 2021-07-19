import sqlite3
import json
from models import Employee

EMPLOYEES = [
    {
        "id": 1,
        "name": "Dan Fields",
        "locationId": 2
    },
    {
        "id": 2,
        "name": "Josh Roads",
        "locationId": 3
    },
    {
        "id": 3,
        "name": "Kristin Worth",
        "locationId": 2
    },
    {
        "id": 4,
        "name": "Kyle Sanders",
        "locationId": 1
    },
    {
        "name": "Samantha Johnson",
        "locationId": 3,
        "id": 5
    },
    {
        "name": "Justin Smith",
        "locationId": 3,
        "id": 6
    },
    {
        "id": 7,
        "name": "Susan Walters",
        "locationId": 1
    },
    {
        "name": "Ashton Monzi",
        "locationId": 2,
        "id": 8
    }
]

# Old function for EMPLOYEES list above
# def get_all_employees():
#     """Return a list of employees
#     Returns:
#         [List]: list of dictionaries
#     """
#     return EMPLOYEES



# SQL GET function
def get_all_employees():
    """Return a list of employees"""
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:
        # Black box
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        """)

        # Initialize an empty list to hold all employee representations
        employees = []
        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()
        # Iterate list of data returned from database
        for row in dataset:
            # Create an employee instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Employee class imported above.
            employee = Employee(row['id'], row['name'], row['address'],
                                row['location_id'])
            employees.append(employee.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(employees)



# Old function for EMPLOYEES list above
# Function with a single parameter
# def get_single_employee(id):
#     """Return a single employee by Id
#     """
#     # Variable to hold the found employee, if it exists
#     requested_employee = None

#     # Iterate the EMPLOYEES list above. Similar to the
#     # for..of loops used in JavaScript.
#     for employee in EMPLOYEES:
#         # Dictionaires in Python use [] notation to find a key
#         # instead of the dot notation that JS used.
#         if employee["id"] == id:
#             requested_employee = employee

#     return requested_employee



# SQL GET function
def get_single_employee(id):
    """Return a single employee by Id"""
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()
        # Create an employee instance from the current row
        employee = Employee(data['id'], data['name'], data['address'],
                                data['location_id'])

        return json.dumps(employee.__dict__)



# SQL GET with query parameters
def get_employees_by_location(location_id):
    """Returns a list of locations by Id"""
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the info you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        WHERE e.location_id = ?
        """, ( location_id, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'],
                                row['location_id'])
            employees.append(employee.__dict__)

    return json.dumps(employees)


def create_employee(employee):
    """Create a NEW employee
    """
    # Get the id value of the last location in the list
    max_id = EMPLOYEES[-1]["id"]
    # Add 1 to whatever that number is
    new_id = max_id + 1
    # Add an `id` property to the employee dictionary
    employee["id"] = new_id
    # Add the employee dictionary to the list
    EMPLOYEES.append(employee)
    # Return the dictionary with `id` property added
    return employee


def delete_employee(id):
    """Delete an employee by Id
    """
    # Initial -1 value for employee index, in case one isn't found
    employee_index = -1

    # Iterate the EMPLOYEES list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index

    # If the employee was found, use pop() to remove it from the list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)


def update_employee(id, new_employee):
    """Edit an employee by Id
    """
    # Iterate the EMPLOYEES list, but with enumerate() so that
    # you can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Update the value.
            EMPLOYEES[index] = new_employee
            break
