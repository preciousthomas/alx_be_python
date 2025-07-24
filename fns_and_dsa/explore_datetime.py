# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days_to_add):
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

# Part 1: Display current date and time
current_date = display_current_datetime()

# Part 2: Calculate future date
try:
    days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(current_date, days)
except ValueError:
    print("Please enter a valid integer for the number of days.")
