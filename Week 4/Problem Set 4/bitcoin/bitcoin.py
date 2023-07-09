import requests
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    output = response.json()
    try:
        price = float(sys.argv[1]) * output["bpi"]["USD"]["rate_float"]
        print(f"${price:,.4f}")
    except ValueError:
        sys.exit("Command-line argument is not a number")



if __name__ == "__main__":
    main()