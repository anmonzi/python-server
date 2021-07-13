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
    """Return a single location by Id
    """
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


def delete_location(id):
    """Delete a location by Id
    """
    # Initial -1 value for location index, in case one isn't found
    location_index = -1

    # Iterate the LOCATIONS list, but use enumerate() so that you
    # can access the index value of each item
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. Store the current index.
            location_index = index

    # If the location was found, use pop(int) to remove it from the list
    if location_index >= 0:
        LOCATIONS.pop(location_index)
