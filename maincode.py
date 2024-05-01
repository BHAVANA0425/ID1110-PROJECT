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
