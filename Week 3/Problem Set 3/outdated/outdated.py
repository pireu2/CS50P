def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        string = input("Date: ")
        string = string.strip()

        if string.find("/") != -1:
            string = string.split("/")
            try:
                year = int(string[2])
                day = int(string[1])
                month = int(string[0])
            except ValueError:
                continue
        else:
            if string.find(",") == -1:
                continue
            else:
                string = string.replace(",","")
                string = string.split(" ")
                try:
                    year = int(string[2])
                    day = int(string[1])
                    month = months.index(string[0]) + 1
                except ValueError:
                    continue
        if 0 <= day <= 31 and 0 <= month <= 12:
            print(f"{year}-{month:02d}-{day:02d}")
            break


main()