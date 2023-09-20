def a(a1,d,n): #aritmatic_sequence
    series_sum = (float(n) * (2 * float(a1) + (float(n) - 1) * float(d))) / 2
    return (series_sum)
def g(g1, q, n): #geometic_series
    if q == 1: # when ratio is one number g1 won't change so assign sepcial case
        return g1 * n
    else:
        series_sum = float(g1) * (1 - float(q) ** float(n)) / (1 - float(q))
        return series_sum
    return (sum_gs)

choice = input("Do you want to callculate a arithmatic(a) or geometric(g) sequence/series")
if choice.lower() == "a":
    a1 = input ("What is the first term(a1)?")
    d = input("What is the difference(d)?")
    n = input("what is the number(n) of terms?")
    result_as = a(a1, d, n)
    print("Den aritmetiska summan är: ",result_as)

else:
    g1 = input("What is the first term(g1)?")
    q = input("What is the factor(q)?")
    n = input("what is the number(n) of terms?")
    result_gs = g(g1, q, n)
    print("Den geometriska summan är: ",result_gs)


