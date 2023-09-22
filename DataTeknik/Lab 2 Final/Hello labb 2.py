def series_sum_arithmetic(a1, d, n):
    Aseries_sum = (n * (2 * a1 + (n - 1) * d)) / 2
    return Aseries_sum
def series_sum_geometric(g1, q, n):
    if q == 1:
        return g1 * n
    else:
        ssg = g1 * (1 - q ** n) / (1 - q)
        return ssg

while True:
    a1_input = input("Skriv in startvärdet (a1): ")
    try:
        a1 = float(a1_input) #För att lösa mitt problem med at a1 lästes som str, omvandlar jag a1 direkt till float genom att ge a1 titeln a1 input i början av koden
        break
    except ValueError:#när fel värdetyp ges i a1_input så ges denna output
        print("Det där var inte ett flyttal. Starta om programmet och försök igen.")

while True:
    d_input = input("Skriv in differansen (d): ")
    try:
        d = float(d_input)
        break
    except ValueError:
        print("Det där var inte ett flyttal. Starta om programmet och försök igen.")

print(" ")

while True:
    g1_input = input("Skriv in startvärdet (g1): ")
    try:
        g1 = float(g1_input)
        break
    except ValueError:
        print("Det där var inte ett flyttal. Starta om programmet och försök igen.")

while True:
    q_input = input("Skriv in kvoten (q): ")
    try:
        q = float(q_input)
        break
    except ValueError:
        print("Det där var inte ett flyttal. Starta om programmet och försök igen.")

print("Antal termer i summorna:")
while True:
    n_input = input("Skriv in antal element i följden (n): ")
    try:
        n = int(n_input)
        break
    except ValueError:
        print("Det där var inte ett heltal. Starta om programmet och försök igen.")

resultA = series_sum_arithmetic(a1, d, n)
resultG = series_sum_geometric(g1, q, n)

if resultA > resultG:
    print("Den aritmetiska summan är störst.")
elif resultG == resultA:
    print("Den aritmetiska och geometriska summan har samma värde.")
else:
    print("Den geometriska summan är störst.")