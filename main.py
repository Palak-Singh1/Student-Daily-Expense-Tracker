# -------------------------------
# Student Daily Expense Tracker
# -------------------------------

expenses = []
next_id = 1


def display_menu():
    print("\n" + "=" * 40)
    print("     Student Daily Expense Tracker")
    print("=" * 40)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. Total Expense")
    print("7. Exit")
    print("=" * 40)


def add_expense():
    global next_id

    amount = float(input("Enter Amount: ₹"))
    category = input("Enter Category: ")
    description = input("Enter Description: ")

    expense = {
        "id": next_id,
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)

    print("\n✅ Expense Added Successfully!")
    print("Expense ID:", next_id)

    next_id += 1


def view_expenses():

    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    print("\n------ All Expenses ------")

    for expense in expenses:
        print(f"""
ID          : {expense['id']}
Amount      : ₹{expense['amount']}
Category    : {expense['category']}
Description : {expense['description']}
------------------------------
""")


def search_expense():

    search_id = int(input("Enter Expense ID: "))

    for expense in expenses:
        if expense["id"] == search_id:
            print("\nExpense Found!")
            print(expense)
            return

    print("Expense not found.")


def update_expense():

    update_id = int(input("Enter Expense ID to Update: "))

    for expense in expenses:

        if expense["id"] == update_id:

            expense["amount"] = float(input("New Amount: ₹"))
            expense["category"] = input("New Category: ")
            expense["description"] = input("New Description: ")

            print("✅ Expense Updated Successfully!")
            return

    print("Expense ID not found.")


def delete_expense():

    delete_id = int(input("Enter Expense ID to Delete: "))

    for expense in expenses:

        if expense["id"] == delete_id:

            expenses.remove(expense)

            print("✅ Expense Deleted Successfully!")
            return

    print("Expense ID not found.")


def total_expense():

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\n💰 Total Expense = ₹{total}")


# ---------------- Main Program ----------------

while True:

    display_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        search_expense()

    elif choice == "4":
        update_expense()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        total_expense()

    elif choice == "7":
        print("\nThank you for using Student Daily Expense Tracker ❤️")
        break

    else:
        print("\nInvalid Choice! Please enter 1-7.")