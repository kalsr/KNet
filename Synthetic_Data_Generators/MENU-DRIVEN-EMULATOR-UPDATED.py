# THIS MENU DRIVEN DATA EMULATOR (EMASS, DITPR, MAPS & ESPS) IS ASSEMBLED BY RANDY SINGH FROM KNet Consulting TO
# SUPPORT DISA OD1 AND OTHER API RELATED DoD MISSIONS.

#python
import json
import random
import uuid

# Helper functions to generate random data
def random_name():
    first_names = ["John", "Jane", "Alice", "Bob", "Charlie"]
    last_names = ["Smith", "Doe", "Johnson", "Williams", "Brown"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def random_email():
    domains = ["example.com", "mail.com", "test.org"]
    return f"{random_name().replace(' ', '.').lower()}@{random.choice(domains)}"

def random_address():
    streets = ["Main St", "High St", "Maple Ave", "Oak St", "Pine St"]
    cities = ["Springfield", "Riverside", "Greenville", "Fairview", "Madison"]
    return f"{random.randint(100, 999)} {random.choice(streets)}, {random.choice(cities)}, USA"

def random_word():
    words = ["alpha", "beta", "gamma", "delta", "epsilon"]
    return random.choice(words)

def random_phone_number():
    return f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"

def random_company():
    companies = ["TechCorp", "BizSolutions", "Innovate LLC", "Alpha Inc", "Global Ventures"]
    return random.choice(companies)

def random_url():
    urls = ["https://example.com", "https://mysite.com", "https://website.org"]
    return random.choice(urls)

def random_latitude():
    return round(random.uniform(-90, 90), 6)

def random_longitude():
    return round(random.uniform(-180, 180), 6)

def random_city():
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
    return random.choice(cities)

def random_product_name():
    products = ["Widget", "Gadget", "Doodad", "Thingamajig", "Contraption"]
    return random.choice(products)

def random_price():
    return round(random.uniform(10, 1000), 2)

def random_category():
    categories = ["Electronics", "Furniture", "Clothing", "Books", "Toys"]
    return random.choice(categories)

# Define schemas for each data emulator
def generate_emass_record():
    return {
        "id": str(uuid.uuid4()),
        "name": random_name(),
        "email": random_email(),
        "address": random_address(),
        "emass_specific_field": random_word()
    }

def generate_ditpr_record():
    return {
        "id": str(uuid.uuid4()),
        "company": random_company(),
        "phone_number": random_phone_number(),
        "website": random_url(),
        "ditpr_specific_field": random_word()
    }

def generate_maps_record():
    return {
        "id": str(uuid.uuid4()),
        "latitude": random_latitude(),
        "longitude": random_longitude(),
        "location_name": random_city(),
        "maps_specific_field": random_word()
    }

def generate_esps_record():
    return {
        "id": str(uuid.uuid4()),
        "product_name": random_product_name(),
        "price": random_price(),
        "category": random_category(),
        "esps_specific_field": random_word()
    }

# Menu options
menu = {
    "1": {"name": "EMASS", "generator": generate_emass_record},
    "2": {"name": "DITPR", "generator": generate_ditpr_record},
    "3": {"name": "MAPS", "generator": generate_maps_record},
    "4": {"name": "ESPS", "generator": generate_esps_record},
    "5": {"name": "Exit"}
}

def main():
    while True:
        print("Select a data emulator:")
        for key, value in menu.items():
            print(f"{key}. {value['name']}")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Exiting program.")
            break

        if choice not in menu or choice == "5":
            print("Invalid choice. Please try again.")
            continue

        try:
            num_records = int(input("Enter the number of records to generate: "))
        except ValueError:
            print("Invalid number. Please try again.")
            continue

        if num_records <= 0:
            print("Number of records must be positive. Please try again.")
            continue

        # Generate records
        records = [menu[choice]["generator"]() for _ in range(num_records)]

        # Save to output file
        output_filename = f"{menu[choice]['name']}.output.json"
        with open(output_filename, 'w') as f:
            json.dump(records, f, indent=4)

        print(f"Generated {num_records} records for {menu[choice]['name']} and saved to {output_filename}")

if __name__ == "__main__":
    main()
#Explanation of FUNCTIONS:

#Loop for Continuous Operation: The program now runs inside a `while` loop that continues until the user selects the "Exit" 
#Exit Option: An "Exit" option is added to the menu (option 5).
# Handling User Input for Exit: If the user selects option 5, the program breaks out of the loop and exits.
# Separate Output Files: Each output file is named according to the selected emulator (e.g., `EMASS.output.json`, `DITPR.output.json`, etc.).

