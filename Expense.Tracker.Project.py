# Expense Tracker Project

expenses = []

# FUNCTIONS 

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food, Travel, Rent, Shopping, etc): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    print("✅ Expense added successfully!\n")


def view_expenses():
    if not expenses:
        print("❌ No expenses recorded.\n")
        return

    print("\n📄 ALL EXPENSES")
    for exp in expenses:
        print("------------------------------")
        print("Date        :", exp["date"])
        print("Category    :", exp["category"])
        print("Description :", exp["description"])
        print("Amount      :", exp["amount"])
    print("------------------------------\n")


def total_expense():
    total = 0
    for exp in expenses:
        total += exp["amount"]

    print("💰 Total Expense:", total, "\n")



def highest_spending_category():
    if not expenses:
        print("❌ No expenses recorded.\n")
        return

    category_total = {}

    for exp in expenses:
        cat = exp["category"]
        amt = exp["amount"]

        if cat in category_total:
            category_total[cat] += amt
        else:
            category_total[cat] = amt

    highest_category = max(category_total, key=category_total.get)
    print("🔥 Highest Spending Category:", highest_category)
    print("Amount Spent:", category_total[highest_category], "\n")


# ------------------ MAIN PROGRAM ------------------

while True:
    print("===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Total Expense")
    print("4. Highest Spending Category")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        highest_spending_category()
    elif choice == "5":
        print("👋 Exiting Expense Tracker")
        break
    else:
        print("❌ Invalid choice. Try again.\n")
