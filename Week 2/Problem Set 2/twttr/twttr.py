def main():
    string = input("Input: ")
    vowels = ["a","A","e","E","i","I","o","O","u","U"]
    for c in vowels:
        string = string.replace(c,"")
    print(f"Output: {string}")

main()