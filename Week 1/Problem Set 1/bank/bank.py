def main():
    string = input("Greeting: ")
    string = string.strip()
    string = string.lower()
    if string.find("hello") != -1:
        print("$0")
    elif string[0] == "h":
        print("$20")
    else:
        print("$100")

main()