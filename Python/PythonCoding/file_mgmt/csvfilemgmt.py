
import csv
import os

# --- Write data to CSV ---
def write_csv(filename):
    data = [
        {"name": "ayush", "age": 20},
        {"name": "aryan", "age": 25}
    ]

    columnnames = ['name','age']
    # Open file in write mode
    with open(filename, "w", newline="\n") as file:
        # Define field names (columns)

        writer = csv.DictWriter(file, fieldnames=columnnames)

        # Write header
        writer.writeheader()

        # Write rows
        writer.writerows(data)
    print(f"Data written to {filename}")


# --- Read data from CSV ---
def read_csv(filename):
    '''if not os.path.exists(filename):
        print(f"{filename} does not exist.")
        return'''

    with open(filename, "r", newline="\n") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Name: {row['name']}, Age: {row['age']}")


# --- Delete CSV file ---
def delete_csv(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted successfully.")
    else:
        print(f"{filename} does not exist.")



filename = "myfile.csv"

write_csv(filename)

print("\nReading data from CSV:")
read_csv(filename)

delete_csv(filename)
