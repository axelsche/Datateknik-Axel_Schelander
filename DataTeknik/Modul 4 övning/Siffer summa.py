import integer_input
N = integer_input.get_integer_input("skriv in ett heltal: ")

def siffersumma(N):
    """Returnerar siffersumman för heltalet tal."""
    if N == 0:
        return 0

    sista_siffran = N % 10
    kvarvarande_siffror = N // 10

    return sista_siffran + siffersumma(kvarvarande_siffror)
print(siffersumma(N))