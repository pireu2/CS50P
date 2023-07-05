def main():
    amount_due = 50
    amount_inserted = 0
    while amount_due > amount_inserted:
        print(f"Amount Due: {amount_due - amount_inserted}")
        x = int(input("Inset Coin: "))
        if  x != 25 and x != 10 and x != 5:
            continue
        amount_inserted += x
    print(f"Change Owed: {amount_inserted - amount_due}")



main()