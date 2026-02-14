import random
import string
import sys

def generate_password(length):
    """
    Creates a random password of a given length.
    Includes letters (upper and lower), digits, and punctuation.
    """
    # Define the set of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters from the set and join them into a string
    password = "".join(random.choice(characters) for i in range(length))
    return password

def main():
    """
    Main function to parse arguments and print the generated password.
    """
    # Check if the length argument is provided via command line
    if len(sys.argv) != 2:
        print("Usage: python main.py <length>")
        sys.exit(1)

    # Validate the length input
    try:
        length = int(sys.argv[1])
        if length <= 0:
            print("Error: Length must be a positive integer.")
            sys.exit(1)
    except ValueError:
        # Handle cases where the input is not a valid integer
        print("Error: Length must be an integer.")
        sys.exit(1)

    # Generate and display the password
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()