import os
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <directory> <prefix> <start_number>")
        sys.exit(1)

    directory = sys.argv[1]
    prefix = sys.argv[2]
    start_number = int(sys.argv[3])

    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' not found.")
        sys.exit(1)

    for i, filename in enumerate(os.listdir(directory)):
        extension = os.path.splitext(filename)[1]
        new_filename = f"{prefix}{start_number + i}{extension}"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

if __name__ == "__main__":
    main()
