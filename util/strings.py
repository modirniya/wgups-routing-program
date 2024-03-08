MAIN_HEADER = """
+-------------------------------------------+
|                                           |
|      WGUPS Delivery Routing Program       |
|                                           |
+-------------------------------------------+
"""

TAG_AT_HUB = 'AT_HUB'
TAG_EN_ROUTE = 'EN_ROUTE'
TAG_DELIVERED = 'DELIVERED'

CSV_PACKAGE_FILE_PATH = './data/csv/package_data.csv'
CSV_DISTANCE_FILE_PATH = './data/csv/distance_data.csv'
CSV_ADDRESS_FILE_PATH = './data/csv/address_data.csv'

# ANSI escape codes for colors
GREEN = '\033[92m'  # Green text
YELLOW = '\033[93m'  # Yellow text
RED = '\033[91m'  # Red text
RESET = '\033[0m'  # Reset to default color

MAIN_MENU = """
    a - Lookup a package
    b - Status of all packages
    q - Quit
    """

TIME_FORMAT_ERROR = "Invalid time format. Please enter the time in HH:MM format or leave empty for default."
START_TIME_PROMPT = "Enter the start time (HH:MM) or press Enter for default:\nType 'q' to go back to the main menu.\n"
END_TIME_PROMPT = "Enter the end time (HH:MM) or press Enter for default:\nType 'q' to go back to the main menu.\n"
