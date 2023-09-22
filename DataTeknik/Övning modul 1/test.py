if 0==0:
    a1 = input("What is the first term(a1)?")
    d = input("What is the difference(d)?")
    print(" ")
    g1 = input("What is the first term(g1)?")
    q = input("What is the factor(q)?")
    print(" ")

n = input("what is the number(n) of terms?")

result_gs = series_sum_geometric(g1, q, n)
result_as = series_sum_arithmatic(a1, d, n)

if n == int:
    print("Aritmatisk summa ",result_as)
    print("Geometrisk summa",result_gs)
else:
    n = input("thats not a whole number, please enter a whole number(n) agian?")

