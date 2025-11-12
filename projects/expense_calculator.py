msg = "Welcome To Expense Calculator"
print(msg)
my_amount = float(input("Enter the total amount: "))
items = []

def view_items(items):
    if not items:
        print("No items to display.")
        return

    print("\nItems List:")
    for item in items:
        print(f"Name: {item['name']}, Rate: {item['rate']}, Quantity: {item['quantity']}, Total: {item['rate'] * item['quantity']}")
    print()

def calculate_balance(my_amount, items):
    total = 0
    for item in items:
        total += item['rate'] * item['quantity']
    balance = my_amount - total

    return balance

while True:
    operations = """
    1. Add New Item
    2. View Items
    3. Balance Amount 
    4. Exit
    """

    operation = int(input(f"Select an operation: {operations}"))

    if operation == 4:
        print("Exiting the Expense Calculator. Goodbye!")
        break

    if operation == 1:
        item = {
            "name": "",
            "rate": 0.0,
            "quantity": 0,
        }

        item["name"] = input("Enter the item name: ")
        item["rate"] = float(input("Enter the item rate: "))
        item["quantity"] = float(input("Enter the item quantity: "))
        items.append(item)

    elif operation == 2:
        view_items(items)

    elif operation == 3:
        balance = calculate_balance(my_amount, items)
        print(f"Your balance amount is: {balance}")

    else:
        print("Invalid operation. Please try again.")            

