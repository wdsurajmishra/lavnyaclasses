msg = """
Time Table Project
You can add your routine here.
1. Add Item
2. View Time Table
3. Exit
"""


time_table = []

def show_time_table(time_table):
    if not time_table:
        print("Time Table is empty.")
        return

    print("\nYour Time Table:")
    print("----------------------------")
    for item in time_table:
        print(f"Time: {item['time']} | Work: {item['work']}")
    print("----------------------------\n")


while True:
    print(msg)
    operation = input("Select an option (1-3): ").strip()

    if operation == "3":
        print("Exiting the Time Table Project. Goodbye!")
        break
    elif operation == "1":
        routine = {
            "time": "",
            "work": ""
        }

        routine["time"] = input("Enter Time (e.g., 9:00 AM - 10:00 AM): ").strip()
        routine["work"] = input("Enter Work/Activity: ").strip()

        time_table.append(routine)
        print("Routine added successfully!")
    elif operation == "2":
        show_time_table(time_table)

    else:
        print("Invalid option. Please select a valid operation (1-3).")
