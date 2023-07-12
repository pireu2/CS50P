def main():
    string = input("Greeting: ")
    print(f"$value(string)")


def value(string):
    string = string.strip()
    string = string.lower()
    if string[:5] == "hello":
        return 0
    elif string[0] == "h" and string[1:5] != "ello":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
