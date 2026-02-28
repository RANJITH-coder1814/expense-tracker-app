import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"

# Load data
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save data
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Add transaction
def add_transaction():
    data = load_data()

    t_type = input("Enter type (income/expense): ").lower()
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Rent, Salary, etc.): ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    transaction = {
        "type": t_type,
        "amount": amount,
        "category": category,
        "date": date
    }

    data.append(transaction)
    save_data(data)
    print("✅ Transaction added successfully!\n")

# View all transactions
def view_transactions():
    data = load_data()
    if not data:
        print("No transactions found.\n")
        return

    for i, t in enumerate(data, start=1):
        print(f"\nTransaction {i}")
        print("Type     :", t["type"])
        print("Amount   :", t["amount"])
        print("Category :", t["category"])
        print("Date     :", t["date"])
    print()

# Show summary
def show_summary():
    data = load_data()
    total_income = sum(t["amount"] for t in data if t["type"] == "income")
    total_expense = sum(t["amount"] for t in data if t["type"] == "expense")
    balance = total_income - total_expense

    print("\n📊 Financial Summary")
    print("----------------------")
    print("Total Income  :", total_income)
    print("Total Expense :", total_expense)
    print("Balance       :", balance)
    print()

# Main menu
def main():
    while True:
        print("===== Expense Tracker =====")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()
