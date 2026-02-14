import os
import sys

# Main function to handle bulk renaming of files in a directory
def main():
    # Check if the correct number of command-line arguments is provided
    # Expected: script name, directory path, prefix string, and starting number
    if len(sys.argv) != 4:
        print("Usage: python main.py <directory> <prefix> <start_number>")
        sys.exit(1)

    # Extract command-line arguments
    directory = sys.argv[1]
    prefix = sys.argv[2]
    # Ensure the start number is an integer
    try:
        start_number = int(sys.argv[3])
    except ValueError:
        print("Error: <start_number> must be an integer.")
        sys.exit(1)

    # Validate if the provided path exists and is a directory
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' not found.")
        sys.exit(1)

    # Iterate through each file in the directory and rename them sequentially
    for i, filename in enumerate(os.listdir(directory)):
        # Get the file extension (e.g., .txt, .jpg)
        extension = os.path.splitext(filename)[1]
        # Generate the new name using prefix and counter
        new_filename = f"{prefix}{start_number + i}{extension}"
        
        # Construct full file paths
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        
        # Perform the rename operation
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")

if __name__ == "__main__":
    main()