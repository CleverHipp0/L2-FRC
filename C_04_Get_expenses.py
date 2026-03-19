import pandas

def statement_generator(statement, decoration):
    """Makes a simple statement look nice by adding a decoration to the beginning and end."""
    print(f"{decoration * 3} {statement} {decoration * 3}")

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

def get_expense(expense_type, quantity_made):
    """This will get a list and return the expenses of the specific type."""
    # List of expenses
    all_items = []
    all_costs = []
    all_amounts = []

    # Avoid errors
    amount = 1
    cost = 0

    expense_dict = {
        "Item": all_items,
        "$ / Item": all_costs,
        "# Bought": all_amounts,
    }

    # Loop until they have entered all of their expenses.
    while True:

        # Make sure that the new expense isn't blank.
        new_expense_name = not_blank("Expense Name: ")

        if (expense_type == "Variable" and new_expense_name == "xxx") and len(all_items) == 0:
            print("🚨 ERROR: Sorry but you have an item. You MUST enter at least 1 item. 🚨")
            continue

        elif new_expense_name == "xxx":
            break

        if expense_type == "Variable":
            amount = int_checker(f"How many: ", int, "")


        cost = int_checker("Cost for one: ", float)

        all_items.append(new_expense_name)
        all_amounts.append(amount)
        all_costs.append(cost)

    expense_frame = pandas.DataFrame(expense_dict)

    expense_frame['$ Cost'] = expense_frame['$ / Item'] * expense_frame['# Bought']

    subtotal = sum(expense_frame['$ Cost'])

    expense_string = expense_frame.to_string(index=False)


    return expense_string, subtotal



# Main routine
# For testing
statement_generator("Variable Expenses", "=")
variable_expenses = get_expense("Variable", 5)
statement_generator("Fixed Expenses", "=")
fixed_expenses = get_expense("Fixed", 5)
print()
print(variable_expenses)
print()
print(fixed_expenses)

# Main routine goes here
