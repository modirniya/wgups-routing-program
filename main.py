# Author: Parham Modirniya
# Student ID: 00927XXXX

from delivery_hub import DeliveryHub
from util.strings import *
from util.time import is_valid_time_or_empty

if __name__ == '__main__':
    print(MAIN_HEADER)  # Print the main header of the program
    hub = DeliveryHub()  # Create a new instance of the DeliveryHub class
    hub.start_delivery_operation()  # Start the delivery operation

    while True:  # Main loop for user interaction
        entry = input(MAIN_MENU)  # Display the main menu and get user input
        if entry.lower() == 'a':  # Option A: Lookup a package
            entry = input("Enter the package ID:  ")  # Prompt for package ID
            if entry.isdigit():  # Check if the input is a valid number
                hub.lookup_package(int(entry))  # Look up the package by ID

        elif entry.lower() == 'b':  # Option B: Generate a report
            while True:  # Loop for getting report time range
                start_entry = input(START_TIME_PROMPT)  # Prompt for start time
                if start_entry.lower() == 'q':  # Check if the user wants to quit
                    break  # Exit the loop
                elif is_valid_time_or_empty(start_entry):  # Validate start time format
                    end_entry = input(END_TIME_PROMPT)  # Prompt for end time
                    if is_valid_time_or_empty(end_entry):  # Validate end time format
                        hub.generate_report(start_time=start_entry if start_entry else "00:00" , end_time=end_entry if end_entry else "17:00")  # Generate the report
                    else:
                        print(TIME_FORMAT_ERROR)  # Print error message for invalid end time format
                else:
                    print(TIME_FORMAT_ERROR)  # Print error message for invalid start time format

        elif entry.lower() == 'q':  # Option Q: Quit the program
            break  # Exit the main loop
