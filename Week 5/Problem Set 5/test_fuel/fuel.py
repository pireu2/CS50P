import sys


def main():
    fraction = input("Input: ")
    x = convert(fraction)
    print(x)



def convert(fraction):
        try:
            fraction = fraction.split("/")
            x = int(fraction[0])
            y = int(fraction[1])
            ratio = x/y
            if ratio > 1:
                raise ValueError
            else:
                return ratio * 100
        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError


def gauge(percentage):
    try:
        if percentage >= 99:
            return "F"
        elif percentage <= 1:
            return "E"
        else:
            return f"{percentage:.0f}%"
    except TypeError:
        raise TypeError


if __name__ == "__main__":
    main()
