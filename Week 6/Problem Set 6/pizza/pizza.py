import sys
import csv
from tabulate import tabulate


def main():
    check_input()
    pizza = []
    with open(f"{sys.argv[1]}", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            pizza.append(row)
        print(tabulate(pizza, headers="keys", tablefmt="grid"))



def check_input():
    if len(sys.argv) == 1 :
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    name, extension = sys.argv[1].split(".")
    if extension != "csv":
        sys.exit("Not a CSV file")
    try:
        open(f"{sys.argv[1]}", "r")
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()