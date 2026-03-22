import pandas
from tabulate import tabulate

def statement_generator(statement, decoration):
    """Makes a simple statement look nice by adding a decoration to the beginning and end."""
    return f"{decoration * 3} {statement} {decoration * 3}"

def not_blank(inquiry):
    """Checks whether an answer is not blank."""

    # This repeats the inquiry until it is answered
    while True:
        element = input(inquiry)

        # Checks the length of the answer and outputs an error if it is too short.
        if len(element.strip()) > 0:
            return element
        else:
            print("🚨 ERROR: This Field is required. Please enter a response. 🚨")

def int_checker(question, int_float=int, exit_code=None):
    """Checks if a number is an integer or a float depending on the situation"""

    # Error message set up
    if int_float == int:
        error = "🚨 ERROR: Please enter an integer (whole number) more than zero. 🚨"
    else:
        error = "🚨 ERROR: Please enter a number more than zero. 🚨"


    while True:
        # Strips unnecessary character
        result = input(question).strip(r"\ ")

        # If the exit code is entered, exit.
        if result.lower() == exit_code and exit_code is not None:
            return result.lower()


        else:
            # Converts result to int or float if possible, else it prints an error.
            try:

                if int_float(result) > 0:
                    return int_float(result)
                else:
                    print(error)

            except ValueError:
                print(error)

def get_expense(expense_type, quantity_needed=1):
    """This will get a list and return the expenses of the specific type."""
    # List of expenses
    all_items = []
    all_costs = []
    all_amounts = []

    # Avoid errors
    amount = 0

    expense_dict = {
        "Item": all_items,
        "$/Item": all_costs,
        "# Bought": all_amounts,
    }

    # Loop until they have entered all of their expenses.
    while True:

        # Make sure that the new expense isn't blank.
        new_expense_name = not_blank("Expense Name: ")

        # Error if it is in variable mode and nothing is entered and exit code is entered.
        if expense_type == "Variable" and new_expense_name == "xxx" and len(all_items) == 0:
            print("🚨 ERROR: Sorry but you have an item. You MUST enter at least 1 item. 🚨")
            continue

        # Exit code.
        elif new_expense_name == "xxx":
            break

        # Asks how many the user needs of each variable expense.
        if expense_type == "Variable":
            amount = int_checker(f"How many <enter for {quantity_needed}>: ", int, "")
            cost = int_checker("Cost for one: $", float)
        else:
            cost = int_checker("Cost: $", float)

        if amount == "":
            amount = quantity_needed

        # Append items to pandas lists.
        all_items.append(new_expense_name)
        all_amounts.append(amount)
        all_costs.append(cost)

    # Pandas
    expense_frame = pandas.DataFrame(expense_dict)

    # Total item cost.
    expense_frame['Cost'] = expense_frame['$/Item'] * expense_frame['# Bought']

    # Subtotal
    subtotal = sum(expense_frame['Cost'])

    # Apply currency formating.
    add_dollars = ['Cost', '$/Item']
    for var_item in add_dollars:
        expense_frame[var_item] = expense_frame[var_item].apply(currency)

    # Make expense frame a string with the desired columns
    if expense_type == "Variable":
        expense_string = tabulate(expense_frame, headers="keys", tablefmt="psql", showindex=False)
    else:
        expense_string = tabulate(expense_frame[["Item", "Cost"]], headers="keys", tablefmt="psql", showindex=False)


    # To string.
    if len(all_items) == 0:
        expense_string = ""


    # Return important stuff.
    return expense_string, subtotal

def currency(x):
    """Currency format 2dp"""
    return f"{x:.2f}"


# Main routine.
# Get the quantity being made.
quantity = int_checker("How many are being made? ", int)


# Heading.
print(statement_generator("Variable Expenses", "="))
# Get variable expenses.
variable_expenses = get_expense("Variable", quantity)

# Heading.
print(statement_generator("Fixed Expenses", "="))

# Get fixed expenses.
fixed_expenses = get_expense("Fixed")

# Output.
# Table variable expenses
variable_pandas = variable_expenses[0]
variable_subtotal = variable_expenses[1]
print(f'{statement_generator("Variable Expenses", "=")}\n')
print(variable_pandas)

# Table fixed expenses
fixed_pandas = fixed_expenses[0]
fixed_subtotal = fixed_expenses[1]
if fixed_pandas != "":
    print(f'{statement_generator("Fixed Expenses", "=")}')
    print(fixed_pandas)

print(f'''
Variable subtotal: {variable_subtotal:.2f}
Fixed subtotal: {fixed_subtotal:.2f}
Total: {(fixed_subtotal+variable_subtotal):.2f}
''')