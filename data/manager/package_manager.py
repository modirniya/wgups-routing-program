import csv
from data.model.package import Package
from data.model.package_status import PackageStatus
from ds.hash_map import HashMap
from util.strings import CSV_PACKAGE_FILE_PATH, TAG_AT_HUB


class PackageManager:
    def __init__(self):
        # Initialize a HashMap to store package data
        self.packages = HashMap()
        # Load package data from CSV file
        self._load_packages_from_csv()

    def __getitem__(self, package_id) -> Package:
        # Retrieve a Package object by its ID
        return self.packages[package_id]

    def __iter__(self):
        # Iterate over all packages, sorted by package ID
        sorted_packages = sorted(self.packages.values(), key=lambda package: package.package_id)
        for package in sorted_packages:
            yield package

    def _load_packages_from_csv(self):
        # Read and process the CSV file containing package data
        with open(CSV_PACKAGE_FILE_PATH) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                package_id = int(row[0])
                package = Package(
                    package_id=package_id,
                    address_id=int(row[1]),
                    delivery_deadline=row[2],
                    weight=int(row[3]),
                    notes=row[4] if row[4] else None
                )
                package.update_status(PackageStatus(TAG_AT_HUB, package_id))
                self.packages[package_id] = package
        # Uncomment the following line if you want to print a confirmation message
        # print("Package data successfully loaded.")

    def update_package_address(self, package_id, address_id):
        # Update the address ID of a package
        self[package_id].address_id = address_id
