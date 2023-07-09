def main():
    message = ["Adieu, adieu, to "]
    while True:
        try:
            name = input()
            message.append(name)
        except EOFError:
            break
    n = len(message)

    print(f"{message[0]}", end = "")
    if n == 2:
        print(f"{message[1]}")
    elif n == 3:
        print(f"{message[1]} and {message[2]}")
    else:
        for i in range(n):
            if 0 < i < n - 1:
                print(f"{message[i]}, ", end = "")
            elif i == n - 1:
                print(f"and {message[i]}")



if __name__ == "__main__":
    main()
