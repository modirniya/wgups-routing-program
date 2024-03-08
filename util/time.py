import re


def decimal_to_hours_minutes(decimal_hours):
    hours = int(decimal_hours)
    minutes = int((decimal_hours - hours) * 60)
    return hours, minutes


def calculate_time_taken_by_distance(distance, current_time: str):
    hour, minute = current_time.split(":")
    hour = int(hour)
    minute = int(minute)
    time_taken = decimal_to_hours_minutes(distance / 18)
    minute += time_taken[1]
    if minute > 59:
        hour += 1
        minute -= 60
    hour += time_taken[0]
    # minute = format_time_unit(minute)
    # hour = format_time_unit(hour)
    return f"{hour:02d}:{minute:02d}"


def add_time(augend_time, addend_time):
    augend_minutes = convert_to_minutes(augend_time)
    addend_minutes = convert_to_minutes(addend_time)
    return convert_minutes_to_time(augend_minutes + addend_minutes)


def calculate_time_difference(departure_time, return_time):
    # Convert the times to minutes
    departure_minutes = convert_to_minutes(departure_time)
    return_minutes = convert_to_minutes(return_time)

    # Calculate the difference in minutes
    diff_minutes = return_minutes - departure_minutes

    # Convert the difference back to HH:MM format
    return convert_minutes_to_time(diff_minutes)


def convert_minutes_to_time(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    return f"{hours:02d}:{minutes:02d}"


def convert_to_minutes(time):
    return int(time.split(':')[0]) * 60 + int(time.split(':')[1])


def is_later(current_time, target_time):
    current_minutes = convert_to_minutes(current_time)
    target_minutes = convert_to_minutes(target_time)
    return target_minutes > current_minutes


def is_valid_time(time_str):
    parts = time_str.split(":")
    if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
        hours, minutes = int(parts[0]), int(parts[1])
        return 0 <= hours <= 23 and 0 <= minutes <= 59
    return False


def is_valid_time_or_empty(time_str):
    return re.match(r'^(\d{2}:\d{2})?$', time_str)