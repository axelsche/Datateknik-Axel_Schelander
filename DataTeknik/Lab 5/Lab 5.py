import integer_input #importerrar heltalsmodelen från tidigare labbar

def search_student_by_id(student_list, id_number_to_find):
    for student in student_list:
        if student["id_number"] == id_number_to_find:
            return student
    return None

#startar listan med studentinformation
school = []

# Ger användaren möjligheten att välja hur många elvers information som ska mattas in
num_students = integer_input.get_integer_input("Hur många elevers information vill du skriva-in? ")

# Loop för input av studentinformation
for i in range(num_students):
    first_name = input("Studentens Förnamn {}:".format(i + 1))#felhantering av namn som limiterar input till strängar med text skulel reducera klodens användbarhet till namn som T.Ex X Æ A-12
    last_name = input("Studentens Efternamn {}:".format(i + 1))
    id_number = integer_input.get_integer_input("Studentents personnumer {}:".format(i + 1))
    print("")
    print ("Objekt skapats")
    print("")


    #skapar student uppslagsvärket
    student_info = {
        "first_name": first_name,
        "last_name": last_name,
        "id_number": id_number
    }

    # lägertill studentinformationen till school skapad tidigare
    school.append(student_info)


# funktionen som låter användare söka efter elever i uppslagsvärket med deras personnummer
def search_student_by_id(student_list, id_number_to_find):
    for student in student_list:
        if student["id_number"] == id_number_to_find:
            return student
    return None


while True:
    # frågar användaren om den vill söka efter elever i upslagsvörket
    listinput = input("Vill du söka efter elever i listan? ja (j) nej (n): ")

    if listinput.lower() == 'j':
        # leter efter studenter givet deras perssonnummer
        search_id = input("Vad är elleven du letar efters personnumer: ")
        found_student = search_student_by_id(school, search_id)

        if found_student:
            print("student hittad:")
            print("Namn: {} {}".format(found_student["first_name"], found_student["last_name"]))
            print("Personnummer: {}".format(found_student["id_number"]))
        else:
            print("Studenten med det givna perssonnumeret är inte en della av studentlistan.")
        break
    elif listinput.lower() == 'n':
        #Om användaren inte vill söka efter elever så printas hela listan med elver till användaren och koden slutar
        print("")
        print("Studentlistan:")
        for student in school:
            print(
                "Name: {} {}, Personnummer: {}".format(student["first_name"], student["last_name"], student["id_number"]))
        break
    else:#om användaren inte skriver n eller j (case spelar ingen roll) så kör lopen igne och frågar om j eller n
        print("fel input, skriv (j) eller (n) för att forsäta")


"""Vilka nackdelar och fördelar finns det med olika behållare"""
"""denom att använda ett upslagsvörk kan den informationen som är satt till en viss ellev eller objekt i koden avöndas som 
sökmål för skningar i koden som i detta fall för att söka efter namn med the länkade personnummer, det skulle vara lättare att skriva 
T.ex en list men detta skulle kräva att en lista per student var skappad i en störe lista där studentens lista (student1 list)
är det som kallas på istälet för ellevens namn eller personnummer"""