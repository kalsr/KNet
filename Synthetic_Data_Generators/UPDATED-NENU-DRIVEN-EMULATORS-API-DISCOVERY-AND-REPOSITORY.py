# THIS PYTHON CODE IS NOW Adding API Discovery, API Repository, and Display API Repository as well 
# ALONG WITH ALL THE EMU;ATORS AND using expanded schemas for each emulator type.
# THIS MENU DRIVEN DATA EMULATOR (EMASS, DITPR, MAPS & ESPS) IS ASSEMBLED BY RANDY SINGH FROM KNet Consulting TO
# SUPPORT DoD OD1 AND OTHER API RELATED DISA MISSIONS.


#python
import json
import os
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

# Define expanded schemas for each data emulator
def generate_emass_record():
    return {
        "id": str(uuid.uuid4()),
        "name": random_name(),
        "email": random_email(),
        "address": random_address(),
        "phone_number": random_phone_number(),
        "company": random_company(),
        "api_url": random_url(),
        "description": random_word(),
        "emass_specific_field": random_word()
    }

def generate_ditpr_record():
    return {
        "id": str(uuid.uuid4()),
        "company": random_company(),
        "phone_number": random_phone_number(),
        "website": random_url(),
        "contact_name": random_name(),
        "contact_email": random_email(),
        "service_description": random_word(),
        "api_endpoint": random_url(),
        "ditpr_specific_field": random_word()
    }

def generate_maps_record():
    return {
        "id": str(uuid.uuid4()),
        "latitude": random_latitude(),
        "longitude": random_longitude(),
        "location_name": random_city(),
        "map_url": random_url(),
        "api_key": str(uuid.uuid4()),
        "service_name": random_word(),
        "maps_specific_field": random_word()
    }

def generate_esps_record():
    return {
        "id": str(uuid.uuid4()),
        "product_name": random_product_name(),
        "price": random_price(),
        "category": random_category(),
        "api_version": f"v{random.randint(1, 3)}",
        "developer_name": random_name(),
        "developer_email": random_email(),
        "service_description": random_word(),
        "api_base_url": random_url(),
        "esps_specific_field": random_word()
    }

# Menu options
menu = {
    "1": {"name": "EMASS", "generator": generate_emass_record},
    "2": {"name": "DITPR", "generator": generate_ditpr_record},
    "3": {"name": "MAPS", "generator": generate_maps_record},
    "4": {"name": "ESPS", "generator": generate_esps_record},
    "5": {"name": "API Discovery"},
    "6": {"name": "Move to API Repository"},
    "7": {"name": "Display API Repository"},
    "8": {"name": "Exit"}
}

# Global variable to keep track of API repository
api_repository = []

def list_json_files():
    return [file for file in os.listdir('.') if file.endswith('.json') and '-' in file]

def discover_apis():
    files = [file for file in list_json_files() if 'Discovered-APIs' not in file]
    if not files:
        print("No output JSON files found.")
        return

    print("Select a file to discover APIs from:")
    for idx, file in enumerate(files):
        print(f"{idx + 1}. {file}")
    
    try:
        choice = int(input("Enter your choice: ")) - 1
        if choice < 0 or choice >= len(files):
            print("Invalid choice. Returning to menu.")
            return
    except ValueError:
        print("Invalid input. Returning to menu.")
        return

    file_to_discover = files[choice]
    with open(file_to_discover, 'r') as f:
        data = json.load(f)

    discovered_apis = [record for record in data if 'api_url' in record or 'api_endpoint' in record or 'map_url' in record or 'api_base_url' in record]
    output_filename = file_to_discover.replace('.json', '-Discovered-APIs.json')
    
    with open(output_filename, 'w') as f:
        json.dump(discovered_apis, f, indent=4)

    print(f"Discovered APIs saved to {output_filename}")

def move_to_api_repository():
    discovered_api_files = list(set(file for file in list_json_files() if 'Discovered-APIs' in file))

    if not discovered_api_files:
        print("No discovered API JSON files found.")
        return

    print("Select a file to move to API repository or choose to move all:")
    for idx, file in enumerate(discovered_api_files):
        print(f"{idx + 1}. {file}")
    print(f"{len(discovered_api_files) + 1}. Move all")

    try:
        choice = int(input("Enter your choice: ")) - 1
        if choice < 0 or choice > len(discovered_api_files):
            print("Invalid choice. Returning to menu.")
            return
    except ValueError:
        print("Invalid input. Returning to menu.")
        return

    if choice == len(discovered_api_files):
        for file in discovered_api_files:
            with open(file, 'r') as f:
                data = json.load(f)
            api_repository.extend(data)
        print("All discovered API files moved to repository.")
    else:
        file_to_move = discovered_api_files[choice]
        with open(file_to_move, 'r') as f:
            data = json.load(f)
        api_repository.extend(data)
        print(f"{file_to_move} moved to repository.")

def display_api_repository():
    if not api_repository:
        print("API repository is empty.")
        return

    for api in api_repository:
        print(json.dumps(api, indent=4))

    with open('API-REPOSITORY.json', 'w') as f:
        json.dump(api_repository, f, indent=4)

    print("All APIs in repository saved to API-REPOSITORY.json")

def main():
    while True:
        print("Select a data emulator or operation:")
        for key, value in menu.items():
            print(f"{key}. {value['name']}")

        choice = input("Enter your choice (1-8): ")

        if choice == "8":
            print("Exiting program.")
            break

        if choice not in menu:
            print("Invalid choice. Please try again.")
            continue

        if choice == "5":
            discover_apis()
        elif choice == "6":
            move_to_api_repository()
        elif choice == "7":
            display_api_repository()
        else:
            try:
                num_records = int(input(f"Enter the number of records to generate for {menu[choice]['name']}: "))
            except ValueError:
                print("Invalid number. Please try again.")
                continue

            if num_records <= 0:
                print("Number of records must be positive. Please try again.")
                continue

            # Generate records
            records = [menu[choice]["generator"]() for _ in range(num_records)]

            # Save to output file
            output_filename = f"{menu[choice]['name']}-Output.json"
            with open(output_filename, 'w') as f:
                json.dump(records, f, indent=4)

            print(f"Generated {num_records} records for {menu[choice]['name']} and saved to {output_filename}")

if __name__ == "__main__":
    main()
