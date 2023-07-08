def main():
    fraction = get_fraction()
    if fraction >= 0.99:
        print("F")
    elif fraction <= 0.01:
        print("E")
    else:
        print(f"{fraction*100:.0f}%")


def get_fraction():
    while True:
        try:
            string = input("Fraction: ")
            string = string.split("/")
            x = int(string[0])
            y = int(string[1])
            fraction = x/y
            if fraction <= 1:
                return fraction
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


main()