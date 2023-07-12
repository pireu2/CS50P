def main():
    string = input("Input: ")
    print(f"Output: {shorten(string)}");


def shorten(word):
    vowels = ["a","A","e","E","i","I","o","O","u","U"]
    for c in vowels:
        word = word.replace(c,"")
    return word



if __name__ == "__main__":
    main()
