import re
import sys
import inflect
from datetime import date
from datetime import timedelta



def main():
    str = input("Date of Birth: ")
    print(convert(str))

def convert(s):
    match = re.fullmatch(r"^(\d\d\d\d)-(\d\d)-(\d\d)$", s)
    if not match:
        sys.exit("Invalid date")
    birth = date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
    today = date.today()
    delta = timedelta()
    delta = today - birth
    minutes = delta.days * 1440
    return inflect.engine().number_to_words(minutes).capitalize().replace(" and", "") + " minutes"


if __name__ == "__main__":
    main()
