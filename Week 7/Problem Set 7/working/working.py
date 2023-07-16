import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    first = re.search(r"^\d?\d(?::\d\d)? (\w\w)", s)
    format = re.search(r"^\d?\d(?::\d\d)? \w\w to (\d?\d(?::\d\d)?) \w\w$", s)
    am = re.search(r"(\d?\d(?::\d\d)?) AM", s)
    pm = re.search(r"(\d?\d(?::\d\d)?) PM", s)
    if format:
        am_time = transform(am.group(1), "AM")
        pm_time = transform(pm.group(1), "PM")
        if first.group(1) == "AM":
            return f"{am_time} to {pm_time}"
        else:
            return f"{pm_time} to {am_time}"
    else:
        raise ValueError

def transform(s, format):
    if ":" in s:
        s_hour, s_minutes = s.split(":")
        s_hour = int(s_hour)
        s_minutes = int(s_minutes)
        if s_hour > 12 or s_minutes > 59:
            raise ValueError
        if s_hour == 12 and format == "AM":
            s_hour = 0
        if s_hour != 12 and format == "PM":
            s_hour += 12
        return f"{s_hour:02}:{s_minutes:02}"
    else:
        s_hour = int(s)
        if s_hour > 12:
            raise ValueError
        if s_hour == 12 and format == "AM":
            s_hour = 0
        if s_hour != 12 and format == "PM":
            s_hour += 12
        return f"{s_hour:02}:00"

if __name__ == "__main__":
    main()
