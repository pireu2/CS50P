def main():
    string = input("What time is it? ")
    x = convert(string)
    if 7 <= x <= 8:
        print("breakfast time")
    elif 12 <= x <= 13:
        print("lunch time")
    elif 18 <= x <= 19:
        print("dinner time")

def convert(string):
    string = string.split()
    time = string[0]
    time = time.split(":")
    if len(string) != 1:
        format = string[1]
        match format:
            case "a.m.":
                y = float(time[0]) + float(time[1])/60
            case "p.m.":
                y = 12 + float(time[0]) + float(time[1])/60
    else :
        y = float(time[0]) + float(time[1])/60
    return y

if __name__ == "__main__":
    main()
