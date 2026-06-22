from functools import reduce


# Get monthly expenses from the user
def get_expenses():
    expenses = []

    number_of_expenses = int(input("How many expenses do you have? "))

    for count in range(number_of_expenses):
        expense_type = input("\nEnter expense type: ")
        expense_amount = float(input("Enter expense amount: $"))

        expenses.append((expense_type, expense_amount))

    return expenses


# Calculate the total expenses using reduce
def calculate_total(expenses):
    total = reduce(
        lambda accumulator, expense: accumulator + expense[1],
        expenses,
        0
    )

    return total


# Find the highest expense
def find_highest(expenses):
    highest = max(expenses, key=lambda expense: expense[1])

    return highest


# Find the lowest expense
def find_lowest(expenses):
    lowest = min(expenses, key=lambda expense: expense[1])

    return lowest


# Main function
def main():
    expenses = get_expenses()

    total_expense = calculate_total(expenses)
    highest_expense = find_highest(expenses)
    lowest_expense = find_lowest(expenses)

    print("\nMonthly Expense Summary")
    print("-----------------------")
    print(f"Total Expenses: ${total_expense:.2f}")

    print(
       f"Highest Expense: {highest_expense[0]} "
       f"(${highest_expense[1]:.2f})"
    )

    print(
    f"Lowest Expense: {lowest_expense[0]} "
    f"(${lowest_expense[1]:.2f})"
    )


# Call the main function
main()