import requests
import csv
import os

def torSearcher(input_csv_path):
    try:
        def get_tor_session():
            session = requests.session()
            # Tor uses the 9050 port as the default socks port
            session.proxies = {'http':  'socks5h://127.0.0.1:9050',
                               'https': 'socks5h://127.0.0.1:9050'}
            return session

        # Read the input CSV file
        with open(input_csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader, None)  # Read the header if it exists

            for row in reader:
                if len(row) > 0:
                    url = row[0]

                    # Make a request through the Tor connection
                    # IP visible through Tor
                    session = get_tor_session()
                    
                    try:
                        print("Getting ...", url)
                        result = session.get(url).text
                    except requests.RequestException as e:
                        print(f"Error during request for {url}: {e}")
                        continue  # Skip to the next URL in case of an error

                    filename = f"html.csv"

                    full_path = os.path.join("Html", filename)
                    directory = os.path.dirname(full_path)

                    if not os.path.exists(directory):
                        os.makedirs(directory)

                    # Open the CSV file in append mode
                    with open(full_path, "a", newline="", encoding="utf-8") as output_csvfile:
                        # Create a CSV writer object
                        csvwriter = csv.writer(output_csvfile)

                        # Write a new row for each URL
                        data = [url, result]
                        csvwriter.writerow(data)

                    print("Data written to the CSV file:", full_path)

    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

# Example usage
torSearcher("sites/drug.csv")
