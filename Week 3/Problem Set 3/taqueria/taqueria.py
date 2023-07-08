def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    getsum(menu)


def getsum(menu):
    sum = 0
    while True:
        try:
            item = input("Item: ")
            item = item.title()
            menu.get(item)
            sum += menu[item]
            print(f"${sum:.2f}")
        except KeyError:
            pass
        except EOFError:
            print()
            return




main()