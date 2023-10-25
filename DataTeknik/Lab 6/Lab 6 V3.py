import integer_input  # Importera modulen för heltal

# Skapa en funktion för att söka efter studenter med ID
def sök_student_efter_id(studentlista, id_nummer_att_hitta):
    for student in studentlista:
        if student["id_number"] == id_nummer_att_hitta:
            return student
    return None

# Skapa en lista för school
school = []

# Skapa en tom dictionary för studentinformation
student_info = {}

# Ladda studentdata från en fil
def ladda_student_data():
    try:
        with open("students.txt", 'r') as fil:
            linjer = fil.readlines()

            # Bearbeta data från filen i set om tre rader
            for i in range(0, len(linjer), 3):
                student_info["id_number"] = linjer[i].strip()
                student_info["last_name"] = linjer[i + 1].strip()
                student_info["first_name"] = linjer[i + 2].strip()

                # Skapa en kopia av dictionary och lägg till den i listan school
                school.append(dict(student_info))

            print("Studentinformation har laddats från filen.")
    except FileNotFoundError:
        print("Ingen tidigare sparad studentinformation hittades.")

# Ladda studentdata från en tidigare session
ladda_student_data()

while True:
    print("Välj ett alternativ:")
    print("1. Importera studentinformation från fil")
    print("2. Lägg till studenter manuellt")
    print("3. Inge fler elever att läggatill")

    val = input("Ange ditt val (1/2/3): ")

    if val == '1':
        # Be användaren om sökväg till filen
        fil_sökväg = input("Ange sökväg till filen: ")

        try:
            with open(fil_sökväg, 'r') as fil:
                linjer = fil.readlines()

                # Bearbeta data i stycken som är tre rader långa
                for i in range(0, len(linjer), 3):
                    student_info["id_number"] = linjer[i].strip()
                    student_info["last_name"] = linjer[i + 1].strip()
                    student_info["first_name"] = linjer[i + 2].strip()

                    # Skapa en kopia av dictionariet och lägger till den i listan school
                    school.append(dict(student_info))

                    print("Studentinformation har importerats från filen.")

        except FileNotFoundError:
            print("Filen hittades inte.")
        except Exception as e:
            print(f"Ett fel inträffade: {str(e)}")

    elif val == '2':
        # Lägg till studenter manuellt och skriv dem till filen
        antal_studenter = integer_input.get_integer_input("Hur många studenters information vill du lägga till? ")

        with open("students.txt", 'a') as fil:
            # Loop för inmatning av studentinformation
            for i in range(antal_studenter):
                student_info["first_name"] = input("Studentens förnamn {}:".format(i + 1))
                student_info["last_name"] = input("Studentens efternamn {}:".format(i + 1))
                student_info["id_number"] = input("Studentens personnummer {}:".format(i + 1))

                # Skapa en kopia av dictionary och lägg till den i listan school
                school.append(dict(student_info))

                # Skriv studentdatan till filen
                fil.write(student_info["id_number"] + "\n")
                fil.write(student_info["last_name"] + "\n")
                fil.write(student_info["first_name"] + "\n")

                print("Studentinformation har lagts till.")

    elif val == '3':
        print("Programmet avslutas.")
        break

    else:
        print("Ogiltigt val. Ange 1, 2 eller 3.")

while True:
    # Fråga användaren om de vill söka efter studenter i listan
    list_input = input("Vill du söka efter studenter i listan? Ja (j) Nej (n): ")

    if list_input.lower() == 'j':
        # Låt användaren söka efter studenter med deras personnummer
        sök_id = input("Ange studentens personnummer du letar efter: ")
        hittad_student = sök_student_efter_id(school, sök_id)

        if hittad_student:
            print("Student hittad:")
            print("Namn: {} {}".format(hittad_student["first_name"], hittad_student["last_name"]))
            print("Personnummer: {}".format(hittad_student["id_number"]))
        else:
            print("Studenten med det angivna personnumret är inte en del av studentlistan.")
    elif list_input.lower() == 'n':
        # Om användaren inte vill söka efter studenter, skriv ut hela listan med studenter och avsluta loopen
        print("Studentlistan:")
        for student in school:
            print("Namn: {} {}, Personnummer: {}".format(student["first_name"], student["last_name"], student["id_number"]))
        break
    else:
        # Om användaren anger ett felaktigt val (inte 'n' eller 'j'), uppmanas de att ange 'n' eller 'j' igen
        print("Ogiltigt val, ange (j) eller (n) för att fortsätta.")



#Komentarer angående koden
"""Vilka nackdelar och fördelar finns det med olika behållare"""
"""denom att använda ett upslagsvörk kan den informationen som är satt till en viss ellev eller objekt i koden avöndas som 
sökmål för skningar i koden som i detta fall för att söka efter namn med the länkade personnummer, det skulle vara lättare att skriva 
T.ex en list men detta skulle kräva att en lista per student var skappad i en störe lista där studentens lista (student1 list)
är det som kallas på istälet för ellevens namn eller personnummer"""

"""Ja använder hashtag komentarer i koden för att det ska gå att skilja på print text och komentarer"""

"""jag anv'nder format föt att ha mer kontrol när det kommer till hur jag printar eftersom jag tar in efternamn
och förnamn individuelt istälet för ett namn"""