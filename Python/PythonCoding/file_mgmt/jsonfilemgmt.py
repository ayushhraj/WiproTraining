
import json
import os

def write_json(filename):
    data = [
        {"name": "ayush", "age": 20},
        {"name": "aryan", "age": 25}
    ]
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
        print(f'Wrote {filename} successfully')


def read_json(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        for person in data["people"]:
            print(f"Name: {person['name']}, Age: {person['age']}")

# def delete_json(filename):
#     if os.path.exists(filename):
#         os.remove(filename)
#         print(f"{filename} deleted successfully.")
#     else:
#         print(f"{filename} does not exist.")

filename = "myfile.json"

write_json(filename)

print("\nReading data from CSV:")
read_json(filename)

#delete_json(filename)