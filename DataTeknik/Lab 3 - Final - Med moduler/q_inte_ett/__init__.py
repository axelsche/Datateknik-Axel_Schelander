def Q_float_not_one(value):
    return isinstance(value, float) and value != 1

if __name__ == "__main__":
    while True:
        try:
            q = float(input("skriv ett flytal: "))
            if Q_float_not_one(q):
                print(f"{q} flyt och inte ett.")
                break
            else:
                print(f"{q} fersök igen.")
        except ValueError:
            print("fersök igen")
