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


def get_all_locations():
    """Return a list of locations

    Returns:
        [List]: list of dictionaries
    """
    return LOCATIONS


# Function with a single parameter
def get_single_location(id):
    # Variable to hold the found location, if it exists
    requested_location = None

    #  Iterate the LOCATIONS list above. Similar to the
    #  for..of loops used in JavaScript.
    for location in LOCATIONS:
        # Dictionaires in Python use [] notation to find a key
        # instead of the dot notation that JS used.
        if location["id"] == id:
            requested_location = location

    return requested_location
