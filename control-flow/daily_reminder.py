def main():
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    reminder = f"Reminder: '{task}' is a {priority} priority task"
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    print(reminder)

if __name__ == "__main__":
    main()
