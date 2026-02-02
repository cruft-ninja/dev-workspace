import requests
import sys

def main():
    """
    Command-line tool to convert currency using the ExchangeRate-API.
    Accepts base currency, target currency, and an amount.
    """
    # Ensure all required command-line arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python main.py <base_currency> <target_currency> <amount>")
        sys.exit(1)

    # Standardize currency codes to uppercase
    base_currency = sys.argv[1].upper()
    target_currency = sys.argv[2].upper()
    
    # Validate that the amount provided is a numeric value
    try:
        amount = float(sys.argv[3])
    except ValueError:
        print("Error: Amount must be a number.")
        sys.exit(1)

    # API endpoint for the specified base currency
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"

    try:
        # Fetch the latest exchange rates
        response = requests.get(url)
        # Check for HTTP request errors
        response.raise_for_status()
        data = response.json()

        # Handle API-specific error responses
        if "error-type" in data:
            print(f"API Error: {data['error-type']}")
            sys.exit(1)
        
        # Check if the target currency exists in the response data
        if target_currency not in data["rates"]:
            print(f"Error: Invalid target currency '{target_currency}'")
            sys.exit(1)

        # Retrieve the conversion rate and calculate the converted total
        conversion_rate = data["rates"][target_currency]
        converted_amount = amount * conversion_rate

        # Print the formatted result
        print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")

    except requests.exceptions.RequestException as e:
        # Catch and report any network or request errors
        print(f"Network error: {e}")
        sys.exit(1)
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()