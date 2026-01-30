import random
import string
import sys

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    return password

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <length>")
        sys.exit(1)

    try:
        length = int(sys.argv[1])
        if length <= 0:
            print("Error: Length must be a positive integer.")
            sys.exit(1)
    except ValueError:
        print("Error: Length must be an integer.")
        sys.exit(1)

    password = generate_password(length)
    print(password)

if __name__ == "__main__":
    main()
