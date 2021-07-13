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


def get_all_employees():
    """Return a list of employees
    Returns:
        [List]: list of dictionaries
    """
    return EMPLOYEES


# Function with a single parameter
def get_single_employee(id):
    """Return a single employee by Id
    """
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the EMPLOYEES list above. Similar to the
    # for..of loops used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaires in Python use [] notation to find a key
        # instead of the dot notation that JS used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

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
