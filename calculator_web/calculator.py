# A Simple Calculator Application
# Demonstrates basic concepts: Variables, Data Types, Data Structures, and Flow Control.

# ----------------- Functions -----------------
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the division of two numbers, handles division by zero."""
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

# ----------------- Main Logic -----------------
def main():
    # 1. DATA TYPES & 2. VARIABLES
    # Data Type: Boolean (used to control our main loop)
    is_running = True
    
    # 3. DATA STRUCTURES
    # Data Structure: List (used to store calculation history)
    history = []

    # Data Type: String
    print("--- Welcome to the Simple Python Calculator ---")

    # 4. FLOW CONTROL: Loop
    while is_running:
        print("\nOperations Menu:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. View History")
        print("6. Exit")

        # Variable: storing user input. The input() function returns a String.
        user_choice = input("Please select an operation (1-6): ")

        # 4. FLOW CONTROL: If-Else Conditions
        if user_choice == '6':
            print("Exiting the calculator. Goodbye!")
            is_running = False  # Update our boolean to break the loop
            
        elif user_choice == '5':
            print("\n--- Calculation History ---")
            # Flow Control: Handle empty history
            if len(history) == 0:
                print("No calculations performed yet.")
            else:
                # Flow Control: For-loop to iterate through history list
                for record in history:
                    print(record)
                    
        elif user_choice in ['1', '2', '3', '4']:
            try:
                # Variables capturing numeric input.
                # Data Type: Float (used to support both decimal and integer math seamlessly)
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                # Flow control: catch error if user doesn't enter a valid number
                print("Error: Invalid input! Please enter numeric values.")
                continue  # Skip to the next iteration of the while loop

            # Variables set to default values
            result = 0
            operation_symbol = ""

            # Flow Control: Route logic based on the selected operation
            if user_choice == '1':
                result = add(num1, num2)
                operation_symbol = "+"
            elif user_choice == '2':
                result = subtract(num1, num2)
                operation_symbol = "-"
            elif user_choice == '3':
                result = multiply(num1, num2)
                operation_symbol = "*"
            elif user_choice == '4':
                result = divide(num1, num2)
                operation_symbol = "/"

            # Formatting Output
            # Flow Control: Check if the result returned an error string (e.g., divide by zero error)
            if isinstance(result, str):
                print(result)
            else:
                # Data Type: String (formatted f-string for display)
                equation = f"{num1} {operation_symbol} {num2} = {result}"
                print(f"\nResult: {equation}")
                
                # Adding the calculation to our list history
                history.append(equation)
                
        else:
            # Handle invalid menu choices correctly
            print("Error: Invalid choice. Please select a valid menu option (1-6).")

# Entry point of the script
if __name__ == "__main__":
    main()
