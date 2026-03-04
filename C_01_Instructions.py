def statement_generator(statement, decoration):
    """Makes a simple statement look nice by adding a decoration to the beginning and end."""
    return f"{decoration * 3} {statement} {decoration * 3}"

def yes_no(inquiry):
    """An even simpler version of my original yes no checker. Asks a question and
    checks if the answer is yes or no."""

    # Error message
    error = "🚨 ERROR: This Field is required. Please enter a 'yes' or 'no' response. 🚨\n"

    # Repats the question like a pesky child until it is correctly answered.
    while True:
        response = input(inquiry).lower().strip()

        # Compares the answer to see whether it is a yes or no.
        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        # If there is no match print an error.
        else:
            print(error)

# Main routine
print(statement_generator("Instruction TEST", "✏️"))

# Ask the user if they want instructions.
skip_instructions = yes_no("Would you like to skip the instructions? ")

# If the user wants instructions print the instructions.
if skip_instructions == "no":
    print(statement_generator("Instructions", "ℹ️"))
    print('''How to climb stairs Safely:
    
    # Set the counter as 0 as the user starts at the bottom.
    steps_climbed = 0
    
    # Loop adding stairs for the amount of stairs in the stair case.
    for steps in staircase:
        steps_climbed += 1
        
    # Let the user know that the completed the task.
    print("You climbed the stairs successfully")
        
    ''')