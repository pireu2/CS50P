import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        mistakes = 0
        x, y = generate_integer(level)
        while True:
            try:
                if mistakes == 3:
                    print(f"{x} + {y} = {x + y}")
                    break
                guess = int(input(f"{x} + {y} = "))
                if guess == x + y:
                    score += 1
                    break
                else:
                    mistakes += 1
                    print("EEE")
            except ValueError:
                mistakes += 1
                print("EEE")
    print(f"Score: {score}")



def get_level():
    while True:
        try:
            x = int(input("Level: "))
            if x == 1 or x == 2 or x == 3:
                return x
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)

    return x, y


if __name__ == "__main__":
    main()
