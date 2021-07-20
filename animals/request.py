from models.location import Location
import sqlite3
import json
from sqlite3 import dbapi2
from models import Animal, Location, Customer

ANIMALS = [
    {
        "id": 1,
        "name": "Doodles",
        "breed": "Poodle",
        "locationId": 3,
        "customerId": 1,
        "status": "Admitted"
    },
    {
        "id": 2,
        "name": "Buster",
        "breed": "Multipoo",
        "customerId": 3,
        "locationId": 1,
        "status": "Admitted"
    },
    {
        "id": 3,
        "name": "Max",
        "breed": "Goldenpoo",
        "locationId": 1,
        "customerId": 4,
        "status": "Admitted"
    },
    {
        "id": 4,
        "name": "Charlie",
        "breed": "Bull Mastif",
        "locationId": 1,
        "customerId": 5,
        "status": "Admitted"
    },
    {
        "id": 5,
        "name": "Meeko",
        "breed": "Mini Poodle",
        "customerId": 4,
        "locationId": 2,
        "status": "Admitted"
    }
]

# Old function for ANIMALS list above (transient state)
# def get_all_animals():
#     """Return a list of animals

#     Returns:
#         [List]: list of dictionaries
#     """
#     return ANIMALS




# SQL GET function
def get_all_animals():
    """Return a list of animals
    Returns:
        [List]: list of dictionaries
    """
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id,
            l.name location_name,
            l.address location_address,
            c.name customer_name,
            c.address customer_address,
            c.email customer_email,
            c.password customer_password
        FROM Animal a
        JOIN Location l
            ON l.id = a.location_id
        JOIN Customer c
            ON c.id = a.customer_id
        """)

        # Initialize an empty list to hold all animal representations
        animals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class imported above.
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])
            # Create a Location instance from the current row
            location = Location(row['id'], row['location_name'], row['location_address'])
            # Add the dictionary (like an object on an object) representation of the location to the animal
            animal.location = location.__dict__
            # Create a Customer instance from the current row
            customer = Customer(row['id'], row['customer_name'], row['customer_address'],
                        row['customer_email'], row['customer_password'])
            animal.customer = customer.__dict__
            
            # Add the dictionary representation of the animal to the list
            animals.append(animal.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(animals) # converts Python object into a json string




# Old function for ANIMALS list above (transient state)
# Function with a single parameter
# def get_single_animal(id):
#     """Return a single animal by Id
#     """
#     # Variable to hold the found animal, if it exists
#     requested_animal = None

#     # Iterate the ANIMALS list above. Very similar to the
#     # for..of loops you used in JavaScript.
#     for animal in ANIMALS:
#         # Dictionaries in Python use [] notation to find a key
#         # instead of the dot notation that JavaScript used.
#         if animal["id"] == id:
#             requested_animal = animal

#     return requested_animal




# SQL GET function
def get_single_animal(id):
    """Return a single animal by Id"""
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a 
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        animal = Animal(data['id'], data['name'], data['breed'],
                            data['status'], data['location_id'],
                            data['customer_id'])

        return json.dumps(animal.__dict__)


# SQL GET with query parameters
def get_animals_by_location(location_id):
    """Returns a list of animals by location Id"""
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the info you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a 
        WHERE a.location_id = ?
        """, ( location_id, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])
            animals.append(animal.__dict__)

    return json.dumps(animals)


# SQL GET with query parameters
def get_animals_by_status(status):
    """Returns a list of animals by status"""
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the info you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a 
        WHERE a.status = ?
        """, ( status, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])
            animals.append(animal.__dict__)

    return json.dumps(animals)



def create_animal(animal):
    """Create a NEW animal
    """
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal



# Old function for ANIMALS list above (transient state)
# def delete_animal(id):
#     """Delete an animal by Id
#     """
#     # Initial -1 value for animal index, in case one isn't found
#     animal_index = -1

#     # Iterate the ANIMALS list, but use enumerate() so that you
#     # can access the index value of each item
#     for index, animal in enumerate(ANIMALS):
#         if animal["id"] == id:
#             # Found the animal. Store the current index.
#             animal_index = index

#     # If the animal was found, use pop(int) to remove it from the list
#     if animal_index >= 0:
#         ANIMALS.pop(animal_index)


# SQL DELETE function
def delete_animal(id):
    """Delete an animal by Id"""
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM animal
        WHERE id = ?
        """, ( id, ))


# Old function for ANIMALS list above (transient state)
# def update_animal(id, new_animal):
#     """Edit an animal by Id
#     """
#     # Iterate the ANIMALS list, but use enumerate() so that
#     # you can access the index value of each item
#     for index, animal in enumerate(ANIMALS):
#         if animal["id"] == id:
#             # Found the animal. Update the value.
#             ANIMALS[index] = new_animal
#             break

# SQL PUT funciton
def update_animal(id, new_animal):
    """Edit an animal by Id"""
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE animal
            SET
                name = ?,
                breed = ?,
                status = ?,
                location_id = ?,
                customer_id = ?
        WHERE id = ?
        """, (new_animal['name'], new_animal['breed'], new_animal['status'],
                new_animal['location_id'], new_animal['customer_id'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0 :
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True