a1 = float(1)
d=float(1)
n=float(1)
q=float(1)
g1=float(1)
def series_sum_arithmatic(a1,d,n): #aritmatic_sequence
    series_sum = (n * (2 * a1 + (n - 1) * d)) / 2
    return series_sum
def series_sum_geometric(g1: object, q: object, n: object) -> object: #geometic_series
    if q == 1: # when ratio is one number g1 won't change so assign sepcial case
        series_sum_geometric(g1, q, n) == g1 * n
        return series_sum_geometric(g1, q, n)
    else:
        ssg = float(g1) * (1 - float(q) ** float(n)) / (1 - float(q))
        return series_sum_geometric

while True:
    a1 = input("Skriv in startvärdet (a1)")

    if a1.replace('.', '', 1).isdigit():  # Check if the input is a valid float
        a1 = float(a1)
        break
    else:
        print("Det där var inte ett flyttal. Starta om programmet och försök igen.")

while True:
    d =input("Skriv in differansen (d)")

    if d.replace('.', '', 1).isdigit():  # Check if the input is a valid float
        d = float(d)
        break
    else:
        print("Det där var inte ett flyttal. Starta om programmet och försök igen.")

print(" ")

while True:
    g1 = input("Skriv in startvärdet (g1)")

    if g1.replace('.', '', 1).isdigit():  # Check if the input is a valid float
        g1 = float(g1)
        break
    else:
        print("Det där var inte ett flyttal. Starta om programmet och försök igen.")

while True:
    q =input("Skriv in kvoten (q)")

    if q.replace('.', '', 1).isdigit():  # Check if the input is a valid float
        q = float(q)
        break
    else:
        print("Det där var inte ett flyttal. Starta om programmet och försök igen.")

print("Antal termer i summorna:")
n = input("Skriv in antal element i följden (n):")

resultA = series_sum_arithmatic(a1, d, n)
resultG = series_sum_geometric(g1, q, n)

if float(resultA) > float(resultG):
    print("Den aritmetiska summan är störst.")
elif resultG == ResultA:
    print("Den aritmatiska och geometriska summan har samma värde.")
else:
    print("Den Geometriska summan är störst.")
