def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6 or s[0:2].isdecimal() or not(s.isalnum()):
        return False
    else:
        number = ""
        for c in s:
            if c.isdecimal():
                number = number + c
            if number != "" and c.isalpha():
                return False
        if number != "" and number[0] == "0":
            return False
        return True


main()
