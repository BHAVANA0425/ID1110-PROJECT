from calendar import calendar

from expenses import Expense
import calendar
import datetime

def main():
    print(f"Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = int(input("Enter budget: "))

    #get user input for expense
    expense = get_user_expense()



    #write their expense to a file.
    save_expense_to_file(expense, expense_file_path)

    #read file and summarize expenses
    summarize_expenses(expense_file_path, budget)
def get_user_expense():
    print(f"Getting User Expense")
    expense_name = input("Enter your Expense Name: ")
    expense_amount = float(input("Enter your Expense Amount: "))
    expense_categories = ["Food","Home","Work","Sport","Fun","misc"]

    while True:
        print("select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i+1}.{category_name}")
        value_range = f"[1-{len(expense_categories)}]"

        selected_index = int(input(f"Enter a category number {value_range}:"))-1

        if i in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense

        else:
            print("invalid choice.please try again")





def save_expense_to_file(expense:Expense, expense_file_path):
    print(f"saving user Expense:{expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.category}, {expense.amount}\n")

