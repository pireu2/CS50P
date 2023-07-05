def main():
    string = input("camelCase: ")
    i = 0
    for c in string:
        if c.isupper():
            string = string[:i] + "_" + string[i:]
            i += 1
        i += 1
    string=string.lower()
    print(f"snake_case: {string}")





main()