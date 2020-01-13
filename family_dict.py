my_family = {
    "sister": {
        "name": "Jill",
        "age": 42
    },
    "mother": {
        "name": "Jane",
        "age": 70
    },
    "father": {
        "name": "John",
        "age": 68
    },
    "brother": {
        "name": "Jack",
        "age": 40
    },
    "uncle": {
        "name": "Jim",
        "age": 72
    },
    "aunt": {
        "name": "Jan",
        "age": 71
    }
}

for (key, value) in my_family.items():
    print(f"{value['name']} is my {key} and is {str(value['age'])} years old")
