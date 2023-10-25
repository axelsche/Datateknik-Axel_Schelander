def skriv_ut(medelande, antal_gånger):
    if antal_gånger <= 0:
            return
    print(medelande)
    skriv_ut(medelande,antal_gånger-1)
skriv_ut("hej",50)

