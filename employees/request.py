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