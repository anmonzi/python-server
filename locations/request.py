import sqlite3
import json
from models import Location

LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8485 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Henry Street"
    },
    {
        "name": "Nashville West",
        "address": "Highway 70th South",
        "id": 3
    }
]

# Old function for LOCATIONS list above (transient state)
# def get_all_locations():
#     """Return a list of locations

#     Returns:
#         [List]: list of dictionaries
#     """
#     return LOCATIONS



# SQL GET function
def get_all_locations():
    """Return a list of locations"""
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
            a.address
        FROM location a
        """)

        # Initialize an empty list to hold all location representations
        locations = []
        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()
        # Iterate list of data returned from database
        for row in dataset:
            # Create a location instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Location Class imported above.
            location = Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(locations) # Converts Python object into a json string



# Old function for LOCATIONS list above (transient state)
# Function with a single parameter
# def get_single_location(id):
#     """Return a single location by Id
#     """
#     # Variable to hold the found location, if it exists
#     requested_location = None

#     #  Iterate the LOCATIONS list above. Similar to the
#     #  for..of loops used in JavaScript.
#     for location in LOCATIONS:
#     # Dictionaires in Python use [] notation to find a key
#     # instead of the dot notation that JS used.
#         if location["id"] == id:
#             requested_location = location

#         return requested_location



# SQL GET function
def get_single_location(id):
    """Return a single location by Id"""
    with sqlite3.connect("./kennel.db") as conn:
        # Black box area
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        WHERE l.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()
        # Create a location instance from the current row
        location = Location(data['id'], data['name'], data['address'])

        return json.dumps(location.__dict__)





def create_location(location):
    """Create a NEW location
    """
    # Get the id value of the last location in the list
    max_id = LOCATIONS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the location dictionary
    location["id"] = new_id

    # Add the location dictionary to the list
    LOCATIONS.append(location)

    # Return the dictionary with `id` property added
    return location



# Old function for LOCATIONS list above (transient state)
# def delete_location(id):
#     """Delete a location by Id
#     """
#     # Initial -1 value for location index, in case one isn't found
#     location_index = -1

#     # Iterate the LOCATIONS list, but use enumerate() so that you
#     # can access the index value of each item
#     for index, location in enumerate(LOCATIONS):
#         if location["id"] == id:
#             # Found the location. Store the current index.
#             location_index = index

#     # If the location was found, use pop(int) to remove it from the list
#     if location_index >= 0:
#         LOCATIONS.pop(location_index)


# SQL DELETE function
def delete_location(id):
    """Delete a location by Id"""
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM location
        WHERE id = ?
        """, ( id, ))


# Old function for LOCATIONS list above (transient state)
# def update_location(id, new_location):
#     """Edit a location by Id
#     """
#     # Iterate the LOCATIONS list, but with enumerate() so that
#     # you can access the index value of each item
#     for index, location in enumerate(LOCATIONS):
#         if location["id"] == id:
#             # Found the location. Update the value.
#             LOCATIONS[index] = new_location
#             break


# SQL PUT function
def update_location(id, new_location):
    """Edit a locaiton by Id"""
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE location
            SET
                name = ?,
                address = ?
        WHERE id = ?
        """, (new_location['name'], new_location['address'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True