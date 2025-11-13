
import pandas as pd
from datetime import date
import os

DATA_FILE = "data/expenses.csv"

def add_expense(category, description, amount):
    # Load or initialize DataFrame
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
    else:
        df = pd.DataFrame(columns=["Date", "Category", "Description", "Amount"])

    # Add new expense
    new_expense = {"Date": date.today(), "Category": category, "Description": description, "Amount": amount}
    df = pd.concat([df, pd.DataFrame([new_expense])], ignore_index=True)

    # Save
    df.to_csv(DATA_FILE, index=False)
    print("✅ Expense added successfully!")

def show_summary():
    if not os.path.exists(DATA_FILE):
        print("⚠️ No expenses recorded yet.")
        return
    df = pd.read_csv(DATA_FILE)
    if df.empty:
        print("⚠️ No expenses recorded yet.")
        return
    summary = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    print("\n📊 Expense Summary by Category:")
    print(summary)
    print("\nTotal spent: $", df["Amount"].sum())

def main():
    print("💰 Personal Expense Tracker")
    while True:
        print("\nOptions: [A]dd Expense | [S]how Summary | [Q]uit")
        choice = input("Enter choice: ").strip().lower()
        if choice == 'a':
            cat = input("Category: ")
            desc = input("Description: ")
            try:
                amt = float(input("Amount: "))
            except ValueError:
                print("❌ Invalid amount. Try again.")
                continue
            add_expense(cat, desc, amt)
        elif choice == 's':
            show_summary()
        elif choice == 'q':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
