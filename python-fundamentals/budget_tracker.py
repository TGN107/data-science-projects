def add_transaction(transactions):
    transaction_type = input("Enter type (income/expense): ").lower()
    amount = float(input("Enter amount: "))
    transactions.append({"type": transaction_type, "amount": amount})
    print("Transaction added!")

def calculate_balance(transactions):
    balance = 0
    for transaction in transactions:
        if transaction["type"] == "income":
            balance += transaction["amount"]
        else:
            balance -= transaction["amount"]
    return balance

def budget_tracker():
    transactions = []
    while True:
        print("\n--- Budget Tracker ---")
        print("1. Add Income/Expense")
        print("2. View Balance")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            balance = calculate_balance(transactions)
            print(f"Your current balance is: ${balance:.2f}")
        elif choice == "3":
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    budget_tracker()
