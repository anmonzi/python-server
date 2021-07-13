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


def get_all_customers():
    """Return a list of customers
    Returns:
        [List]: list of dictionaries
    """
    return CUSTOMERS

# Function with a single parameter
def get_single_customer(id):
    """Returns a single customer by Id
    """
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the EMPLOYEES list above. Similar to the
    # for..of loops used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaires in Python use [] notation to find a key
        # instead of the dot notation that JS used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer


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
    