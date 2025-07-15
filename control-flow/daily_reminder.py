# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Generate a reminder using match-case based on priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Note: '{task}' has an unknown priority"

# Modify message based on time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if priority in ["low", "medium", "high"]:
        message += ". Consider completing it when you have free time."

# Print the final reminder
print("\n" + message)
