# Python Program to Extract and Save MAPS-API Data into a file.
# THIS PROGRAM IS ASSEMBLED BY RANDY SINGH KNet Consulting.

#python
import json

def extract_api_data(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            data = json.load(file)

        api_data = [record["API Information"] for record in data if "API Information" in record]

        with open(output_file, 'w') as file:
            json.dump(api_data, file, indent=4)

        print(f"API data has been extracted and saved to {output_file}")

    except FileNotFoundError:
        print(f"File {input_file} not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON from the input file.")
    except KeyError as e:
        print(f"Key error: {e} not found in one of the records.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    input_file = "MAPS_output.json"
    output_file = "MAPS_API_Output.json"
    extract_api_data(input_file, output_file)

if __name__ == "__main__":
    main()
