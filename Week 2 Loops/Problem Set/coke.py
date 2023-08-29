paid = 0

while True:
    inserted = int(input("Insert Coins: "))

    match inserted:
        case 5 | 10 | 25:
            paid += inserted
            if paid >= 50:
                print(f"Change Owed: {paid - 50}")
                break
            else:
                print(f"Amount Due: {50 - paid}")