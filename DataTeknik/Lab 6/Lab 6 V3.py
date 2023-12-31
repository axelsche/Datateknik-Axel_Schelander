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
        with open("student.txt", 'r') as file:
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


# Skapa en funktion för att redigera studentinformation
def redigera_student(studentlista, id_nummer_att_redigera):
    for student in studentlista:
        if student["id_number"] == id_nummer_att_redigera:
            print("Nuvarande information för student:")
            print("Namn: {} {}".format(student["first_name"], student["last_name"]))
            print("Personnummer: {}".format(student["id_number"]))

            # Låt användaren redigera informationen
            student["first_name"] = input("Ange det nya förnamnet: ")
            student["last_name"] = input("Ange det nya efternamnet: ")
            student["id_number"] = input("Ange det nya personnumret: ")

            print("Studentinformation har redigerats.")
            return

    print("Studenten med det angivna personnumret är inte en del av studentlistan.")


# Skapa en funktion för att radera studentinformation
def radera_student(studentlista, id_nummer_att_radera):
    for student in studentlista:
        if student["id_number"] == id_nummer_att_radera:
            studentlista.remove(student)
            print("Studentinformation har raderats.")
            return

    print("Studenten med det angivna personnumret är inte en del av studentlistan.")


ladda_student_data()  # Ladda studentdata från en tidigare session

while True:
    print("Välj ett alternativ:")
    print("1. Importera studentinformation från fil")
    print("2. Lägg till studenter manuellt")
    print("3. Inge fler elever att lägga till")
    print("4. Redigera studentinformation")
    print("5. Radera studentinformation")
    print("6. Avsluta")

    val = input("Ange ditt val (1/2/3/4/5/6): ")

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

                # Skriv student data till filen
                fil.write(student_info["id_number"] + "\n")
                fil.write(student_info["last_name"] + "\n")
                fil.write(student_info["first_name"] + "\n")

                print("Studentinformation har lagts till.")

    elif val == '3':
        print("Programmet avslutas.")
        break

    if val == '4':
        # Låt användaren ange personnummer för att redigera studentinformation
        id_nummer_att_redigera = input("Ange personnumret för studenten du vill redigera: ")
        redigera_student(school, id_nummer_att_redigera)

    elif val == '5':
        # Låt användaren ange personnummer för att radera studentinformation
        id_nummer_att_radera = input("Ange personnumret för studenten du vill radera: ")
        radera_student(school, id_nummer_att_radera)

    elif val == '6':
        print("Programmet avslutas.")
        break

    else:
        print("Ogiltigt val. Ange 1, 2, 3, 4, 5 eller 6.")

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
            print("Namn: {} {}, Personnummer: {}".format(student["first_name"], student["last_name"],
                                                         student["id_number"]))
        break
    else:
        # Om användaren anger ett felaktigt val (inte 'n' eller 'j'), uppmanas de att ange 'n' eller 'j' igen
        print("Ogiltigt val, ange (j) eller (n) för att fortsätta.")

# Kommentarer angående koden
"""Vilka nackdelar och fördelar finns det med olika behållare"""
"""Genom att använda ett uppslagsverk kan den informationen som är satt till en viss student eller objekt i koden 
används som sökmål för sökningar i koden som i detta fall för att söka efter namn med the länkade personnummer, 
det skulle vara lättare att skriva T.ex en list men detta skulle kräva att en lista per student var skapad i en störe 
lista där studentens lista (student1 list) är det som kallas på istället för elevens namn eller personnummer"""

"""Ja använder hashtag kommentarer i koden för att det ska gå att skilja på print text och kommentarer"""

"""jag använder format föt att ha mer kontrol när det kommer till hur jag printar eftersom jag tar in efternamn
och förnamn individual istället för ett namn"""
