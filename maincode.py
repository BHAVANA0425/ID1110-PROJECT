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

def summarize_expenses(expense_file_path, budget):
    print(f"Summarizing user Expense")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_category, expense_amount = line.strip().split(",")
            print(expense_name, expense_category, expense_amount)
            line_expense = Expense(name=expense_name, category=expense_category, amount=float(expense_amount))

            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    print("Expenses by category")
    for key, amount in amount_by_category.items():
        print(f"{key}: ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"you've spent $({total_spent:.2f})this month!")

    remaining_budget = budget - total_spent
    print(f"budget remaining: ${remaining_budget:.2f}")

    #get the current date
    now = datetime.datetime.now()

    #get the number of days in the current month
    days_in_month = calendar.monthrange(now.year, now.month)[1]

    #calculate the remaining number of days in the current month
    remaining_days = days_in_month - now.day

    print("Remaining days in the current month:", remaining_days)


    if remaining_days==0:
        print(f"daily budget=={remaining_budget}")
    else:
        daily_budget = remaining_budget / remaining_days
        print(f"Budget per day: {daily_budget:.2f}")




if __name__ == "__main__":
    main()


