def main():
    d = {}
    while True:
        try:
            item = input()
            item = item.upper()
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        except EOFError:
            break
    d = dict(sorted(d.items()))
    printdict(d)


def printdict(d):
    for i in d:
        print(f"{d[i]} {i}")

main()