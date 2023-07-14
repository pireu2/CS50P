import sys

def main():
    check_input()
    with open(f"{sys.argv[1]}", "r") as file:
        n = 0
        for line in file:
            line = line.strip()
            if not line.startswith("#") and len(line) != 0:
                n += 1
        print(n)


def check_input():
    if len(sys.argv) == 1 :
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    name, extension = sys.argv[1].split(".")
    if extension != "py":
        sys.exit("Not a Python file")
    try:
        open(f"{sys.argv[1]}", "r")
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()