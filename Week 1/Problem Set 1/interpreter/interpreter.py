def main():
    string = input("Expression: ")
    string = string.strip()
    string = string.split()
    x = int(string[0])
    y = int(string[2])
    match string[1]:
        case "+":
            print(f"{x + y:.1f}")
        case "-":
            print(f"{x - y:.1f}")
        case "/":
            print(f"{x / y:.1f}")
        case "*":
            print(f"{x * y:.1f}")


main()