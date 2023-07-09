import random

def main():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except ValueError:
            pass

    x = random.randint(1,level)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < x:
                print("Too small!")
            elif guess == x:
                print("Just right!")
                break
            elif guess > x:
                print("Too large!")
        except ValueError:
            pass

if __name__ == "__main__":
    main()