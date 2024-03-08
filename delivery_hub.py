from data.manager.address_manager import AddressManager
from data.manager.package_manager import PackageManager
from data.manager.routing_manager import RoutingManager
from data.model.deliveryـtruck import DeliveryTruck
from util.time import *


class DeliveryHub:
    def __init__(self):
        # Initialize managers for packages, addresses, and routing
        self.package_manager = PackageManager()
        self.address_manager = AddressManager()
        self.routing_manager = RoutingManager()
        # Define delivery schedules with address IDs and package IDs
        self.morning_schedule_addresses = [22, 3, 5, 6, 7, 13, 16, 18, 19, 20, 21]
        self.morning_schedule_packages = [1, 7, 13, 14, 15, 16, 19, 20, 21, 29, 30, 31, 34, 37, 39, 40]
        self.mid_morning_schedule_addresses = [25, 2, 4, 8, 9, 10, 12, 13, 14, 17, 20, 26]
        self.mid_morning_schedule_packages = [2, 3, 5, 6, 8, 10, 12, 18, 25, 26, 27, 28, 33, 35, 36, 38]
        self.late_morning_schedule_addresses = [23, 11, 13, 15, 16, 19, 24, 27]
        self.late_morning_schedule_packages = [4, 9, 11, 17, 22, 23, 24, 32]
        self.earliest_departure_time = "08:00"
        self.latest_return_time = self.earliest_departure_time
        self.total_drive_time = "00:00"
        self.total_miles = 0

    def __repr__(self):
        operation_time = calculate_time_difference(self.earliest_departure_time, self.latest_return_time)
        border = "+" + "-" * 38 + "+"
        header = f"| {'Delivery Hub Summary':^36} |"
        total_miles = f"| Total miles driven: {self.total_miles:<16} |"
        drive_time = f"| Total drive time: {self.total_drive_time:<18} |"
        departure_time = f"| Earliest departure time: {self.earliest_departure_time:<11} |"
        return_time = f"| Latest return time: {self.latest_return_time:<16} |"
        operation_time_str = f"| Total operation time: {operation_time:<14} |"

        return (
            f"\n{border}\n{header}\n{border}\n"
            f"{total_miles}\n{drive_time}\n{departure_time}\n"
            f"{return_time}\n{operation_time_str}\n{border}\n"
        )

    def start_delivery_operation(self):
        # Initialize trucks
        truck1 = DeliveryTruck(self.package_manager, "1")
        truck2 = DeliveryTruck(self.package_manager, "2")
        # Dispatch trucks with their respective schedules
        self.dispatch_truck(truck1, self.earliest_departure_time,
                            self.morning_schedule_addresses, self.morning_schedule_packages)
        self.dispatch_truck(truck2, "09:05",
                            self.mid_morning_schedule_addresses,
                            self.mid_morning_schedule_packages)
        # Correct the wrong address associated with package #9
        self.late_morning_schedule_addresses.remove(13)
        self.late_morning_schedule_addresses.append(20)
        self.package_manager.update_package_address(9, 20)
        self.dispatch_truck(truck1, "10:21",
                            self.late_morning_schedule_addresses,
                            self.late_morning_schedule_packages)
        # Print delivery hub summary
        print(self)

    def lookup_package(self, package_id):
        package = self.package_manager[package_id]
        address = self.address_manager[package.address_id]
        print(package)
        print(address)

    def generate_report(self, start_time, end_time):
        # Generate a report for all packages up to a specific time
        print(f"Delivery Status Report as of {end_time}")
        print(f"{'Package ID':<8} | {'Status':<4} | {'Time':<4} | {'Truck ID':<4}")
        print("-" * 50)
        for package in self.package_manager:
            for status in reversed(package.delivery_status):
                if start_time <= status.time <= end_time:
                    print(status)
                    break

    def dispatch_truck(self, delivery_truck, start_time, address_ids, package_ids):
        # Calculate the route for the truck
        designated_path = self.routing_manager.route(address_ids)
        # Start the delivery process for the truck
        delivery_truck.start_delivery(start_time, designated_path, package_ids)
        # Update the hub's total drive time and total miles
        self.total_drive_time = add_time(self.total_drive_time, delivery_truck.drive_time)
        self.total_miles += round(delivery_truck.trip_mileage, 1)
        # Update the hub's latest return time if necessary
        if is_later(self.latest_return_time, delivery_truck.return_time):
            self.latest_return_time = delivery_truck.return_time
        # Print the truck's metrics
        print(delivery_truck)
