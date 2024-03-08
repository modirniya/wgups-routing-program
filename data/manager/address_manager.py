import csv
from data.model.address import Address
from ds.hash_map import HashMap
from util.strings import CSV_ADDRESS_FILE_PATH


class AddressManager:
    def __init__(self):
        # Initialize a HashMap to store address data
        self.addresses = HashMap()
        # Load address data from CSV file
        self._load_addresses_from_csv()

    def __getitem__(self, address_id):
        # Retrieve an Address object by its ID
        return self.addresses[address_id]

    def _load_addresses_from_csv(self):
        # Read and process the CSV file containing address data
        with open(CSV_ADDRESS_FILE_PATH) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                address_id = int(row[0])
                address = Address(
                    address_id=address_id,
                    name=row[1],
                    street=row[2],
                    city=row[3],
                    state=row[4],
                    zip_code=row[5]
                )
                self.addresses[address_id] = address
        # Uncomment the following line if you want to print a confirmation message
        # print("Address data successfully loaded.")
