import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <num1> <operator> <num2>")
        sys.exit(1)

    num1 = float(sys.argv[1])
    operator = sys.argv[2]
    num2 = float(sys.argv[3])

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero")
            sys.exit(1)
        result = num1 / num2
    else:
        print("Invalid operator")
        sys.exit(1)

    print(result)

if __name__ == "__main__":
    main()
