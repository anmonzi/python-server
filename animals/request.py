ANIMALS = [
    {
        "id": 1,
        "name": "Doodles",
        "breed": "Poodle",
        "locationId": 3,
        "customerId": 1
    },
    {
        "id": 2,
        "name": "Buster",
        "breed": "Multipoo",
        "customerId": 3,
        "locationId": 1
    },
    {
        "id": 3,
        "name": "Max",
        "breed": "Goldenpoo",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 4,
        "name": "Charlie",
        "breed": "Bull Mastif",
        "locationId": 1,
        "customerId": 5
    },
    {
        "id": 5,
        "name": "Meeko",
        "breed": "Mini Poodle",
        "customerId": 4,
        "locationId": 2
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
