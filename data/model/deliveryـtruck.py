from data.manager.package_manager import PackageManager
from data.manager.routing_manager import RoutingManager
from data.model.package_status import PackageStatus
from util.strings import *
from util.time import calculate_time_taken_by_distance, calculate_time_difference


class DeliveryTruck:
    def __init__(self,
                 pm: PackageManager,
                 truck_id: str):
        self.truck_id = truck_id
        self.package_manager = pm
        self.packages = []
        self.current_time = None
        self.departure_time = None
        self.return_time = None
        self.drive_time = None
        self.trip_mileage = 0
        self.total_mileage = 0

    def __repr__(self):
        border = "+" + "-" * 26 + "+"
        title = f"| Truck #{self.truck_id} metrics |"
        departure = f"| Departure time: {self.departure_time:<10} |"
        return_time = f"| Return time:    {self.return_time:<10} |"
        drive_time = f"| Drive time:     {self.drive_time:<10} |"
        total_miles = f"| Total miles:    {round(self.trip_mileage, 1):<10} |"

        message = f"""
    {border}
    {title}
    {border}
    {departure}
    {return_time}
    {drive_time}
    {total_miles}
    {border}
        """
        return message

    @property
    def mileage(self):
        return self.total_mileage

    def start_delivery(self, time, designated_path, package_ids):
        # 1. Initialize the delivery process
        self.current_time = time  # Set the current time to the specified starting time
        self.trip_mileage = 0  # Reset the trip mileage to 0 for this delivery
        self.departure_time = time  # Record the departure time for this delivery
        # 2. Load packages onto the truck
        for package_id in package_ids:
            package = self.package_manager[package_id]  # Retrieve the package by its ID
            self._load_package(package)  # Load the package onto the truck
        # 3. Travel along the designated path and deliver packages
        for address_id, distance in designated_path:
            self.trip_mileage += distance  # Add the distance to the trip mileage
            self.current_time = (
                calculate_time_taken_by_distance(
                    distance, self.current_time))  # Update the current time based on travel distance
            self._unload_packages_at_address(address_id)  # Unload packages at the current address
        # 4. Finalize the delivery process
        self.return_time = self.current_time  # Record the return time after all deliveries are complete
        self.total_mileage += self.trip_mileage  # Update the total mileage of the truck
        self.drive_time = calculate_time_difference(self.departure_time,
                                                    self.return_time)  # Calculate the total drive time for this delivery

    def _load_package(self, package):
        # Load a package onto the truck and update its status to "EN_ROUTE"
        package.update_status(
            PackageStatus(event=TAG_EN_ROUTE,
                          package_id=package.package_id,
                          time=self.current_time,
                          truck_id=self.truck_id))
        self.packages.append(package)

    def _unload_packages_at_address(self, address_id):
        # Unload packages at a given address and update their statuses
        unloaded_packages = [package for package in self.packages if package.address_id == address_id]
        for package in unloaded_packages:
            package.update_status(PackageStatus(TAG_DELIVERED, package.package_id, self.current_time, self.truck_id))
            self.packages.remove(package)
