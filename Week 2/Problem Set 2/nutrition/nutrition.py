def main():
    string = input("Item: ")
    calories = {
        "apple" : 130,
        "avocado" : 50,
        "banana" : 110,
        "cantaloupe" : 50,
        "grapefruit" : 60,
        "grapes" : 90,
        "honeydew" : 50,
        "kiwifruit" : 90,
        "lemon" : 15,
        "lime" : 20,
        "nectarine" : 60,
        "orange" : 80,
        "peach" : 60,
        "pear" : 100,
        "pineapple" : 50,
        "plums" : 70,
        "strawberries" : 50,
        "sweet" : 100,
        "watrermelon" : 80
    }
    string = string.strip()
    string = string.lower()
    string = string.split()

    for k in calories:
        if k == string[0]:
            print(f"Calories: {calories[k]}")


main()