import requests
from bs4 import BeautifulSoup
import sys

def main():
    """
    Fetches a web page and prints its title.
    Demonstrates basic web scraping using requests and BeautifulSoup.
    """
    # Verify that a URL was provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python main.py <url>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        
        # Raise an exception for HTTP errors (e.g., 404, 500)
        response.raise_for_status()
        
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract and print the content of the <title> tag
        if soup.title:
            print(f"Page Title: {soup.title.string}")
        else:
            print("No title tag found in the document.")

    except requests.exceptions.RequestException as e:
        # Handle network-related errors (e.g., DNS, connection refused)
        print(f"Network error occurred: {e}")
        sys.exit(1)
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()