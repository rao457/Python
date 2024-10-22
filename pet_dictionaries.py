pets = [
    {
        "name": "Monty",
        "species": "Ball Python",
        "age": 3,
        "color": "Normal",
        "favorite_food": "Mice"
    },
    {
        "name": "Spike",
        "species": "Burmese Python",
        "age": 5,
        "color": "Albino",
        "favorite_food": "Rabbits"
    },
    {
        "name": "Ziggy",
        "species": "Green Tree Python",
        "age": 2,
        "color": "Green",
        "favorite_food": "Birds"
    }
]
for pet_number in pets:
    for key, value in pet_number.items():
        print(f"{key} : {value}")
