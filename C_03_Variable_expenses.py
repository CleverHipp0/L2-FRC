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


# Main routine goes here
# List of variable expenses
variable_expenses = []

while True:

    new_expense = not_blank("Variable Expense Name: ")

    if new_expense == "xxx" and len(new_expense) == 0:
        print("🚨 ERROR: Sorry but you have not entered anything. You MUST enter at least 1 value. 🚨")
    elif new_expense == "xxx" and len(new_expense) >= 1:
        break
    else:
        continue
        





