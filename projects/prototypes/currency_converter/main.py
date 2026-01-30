import requests
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <base_currency> <target_currency> <amount>")
        sys.exit(1)

    base_currency = sys.argv[1].upper()
    target_currency = sys.argv[2].upper()
    
    try:
        amount = float(sys.argv[3])
    except ValueError:
        print("Error: Amount must be a number.")
        sys.exit(1)

    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "error-type" in data:
            print(f"Error: {data['error-type']}")
            sys.exit(1)
        
        if target_currency not in data["rates"]:
            print(f"Error: Invalid target currency '{target_currency}'")
            sys.exit(1)

        conversion_rate = data["rates"][target_currency]
        converted_amount = amount * conversion_rate

        print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
