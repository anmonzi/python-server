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


def get_all_animals():
    """Return a list of animals

    Returns:
        [List]: list of dictionaries
    """
    return ANIMALS


# Function with a single parameter
def get_single_animal(id):
    """Return a single animal by Id
    """
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal


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


def delete_animal(id):
    """Delete an animal by Id
    """
    # Initial -1 value for animal index, in case one isn't found
    animal_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Store the current index.
            animal_index = index

    # If the animal was found, use pop(int) to remove it from the list
    if animal_index >= 0:
        ANIMALS.pop(animal_index)


def update_animal(id, new_animal):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Update the value.
            ANIMALS[index] = new_animal
            break
