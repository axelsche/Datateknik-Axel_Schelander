#I denna laboration kommer vi använda oss av en egenskriven modul som vi importerar in i vårt huvudprogram.
#Denna modul ska innehålla två funktioner, en som kontrollerar att inmatningen är ett heltal (int) och en som,
#kontrollerar att inmatningen är ett flyttal (float). De två funktionerna ska ta inmatning från användaren och inte,
#returnera förrän användaren har matat in korrekt data.
def series_sum_arithmetic(A1, D, N):
    Aseries_sum = (N * (2 * A1 + (N - 1) * D)) / 2
    return Aseries_sum
def series_sum_geometric(G1, Q, N):
    if Q == 1:
        return G1 * N
    else:
        ssg = G1 * (1 - Q ^ N) / (1 - Q)
        return ssg

import float_input #importerar min modul som kollar om värdet är ett reelt tal
print("variabler för den aritmetiska summan:")
A1 = float_input.get_float_input("A1: ")
D = float_input.get_float_input("D: ")
print("variabler för den geometriska summan:")
print("")
G1 = float_input.get_float_input("G1: ")
Q = input("q: ")
print("")

import integer_input # importerar min modul som kollar om värdet är ett reelt heltal
print ("Antal termer i summorna(Heltal):")
N = integer_input.get_integer_input("n: ")

print("")

resultA = series_sum_arithmetic(A1, D, N)
resultG = series_sum_geometric(G1, Q, N)

#storleksjämföring av aritmatisk och geometrisk
if resultA > resultG:
    print("Den aritmetiska summan är störst.")
elif resultG == resultA:
    print("Den aritmetiska och geometriska summan har samma värde.")
else:
    print("Den geometriska summan är störst.")
