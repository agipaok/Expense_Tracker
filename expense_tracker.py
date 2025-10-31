# Expense Tracker

expenses = []

def add_expense():
    while True:
        description = str(input("Give description: "))
        amount = input("Give amount: ")
        try:
            amount = float(amount)
            if amount > 0:
                expenses.append((description, amount))
                break
            else:
                print("Amount must be positive!")
                continue
        except ValueError:
            print("Please enter a Valid Number")
            continue


def show_expenses():

    if len(expenses) == 0:
        print("No expenses imported!")
    else:
        for description, expense in expenses:
            print(f"{description} {expense}")

def show_stats():
    user_expenses = []
    max_description = ""
    if len(expenses) == 0:
        print("No expenses imported!")
    else:
        for description, expense in expenses:
            user_expenses.append(expense)
            
            
        exp_avg = sum(user_expenses) / len(user_expenses)
        exp_sum = sum(user_expenses)
        exp_max = max(user_expenses)

        for description, expense in expenses:
            if round(expense,2) == round(exp_max,2):
                max_description = description

        print(f"Your expenses in total are {exp_sum} with average {exp_avg} and the biggest expense is{max_description} who costs {exp_max}")

3
while True:
    print("1.Add expense")
    print("2.Show expenses")
    print("3.Show statistics")
    print("4.Exit")
    user_input = input("> ")

    try:
        if user_input == "1":
            add_expense()
        elif user_input == "2":
            show_expenses()
        elif user_input == "3":
            show_stats()
        elif user_input == "4":
            print("Thank you! Have a nice day")
            break
    except ValueError:
        print("You must choose 1,2,3")



