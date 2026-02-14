import sys

def main():
    """
    A simple command-line calculator.
    Supports basic operations: +, -, *, /
    """
    # Verify that exactly three arguments are provided (num1, operator, num2)
    if len(sys.argv) != 4:
        print("Usage: python main.py <num1> <operator> <num2>")
        sys.exit(1)

    # Parse numeric inputs
    try:
        num1 = float(sys.argv[1])
        operator = sys.argv[2]
        num2 = float(sys.argv[3])
    except ValueError:
        print("Error: Please provide valid numbers for num1 and num2.")
        sys.exit(1)

    # Determine the operation based on the operator provided
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        # Handle division by zero case
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            sys.exit(1)
        result = num1 / num2
    else:
        # Handle unsupported operators
        print(f"Error: Invalid operator '{operator}'. Supported: +, -, *, /")
        sys.exit(1)

    # Display the final result
    print(f"Result: {result}")

if __name__ == "__main__":
    main()