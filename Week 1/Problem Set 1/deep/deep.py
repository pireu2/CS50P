def main():
    string = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    string = string.strip()
    string = string.lower()
    match string:
        case "forty two" | "forty-two" | "42":
            print("Yes")
        case _:
            print("No")






main()