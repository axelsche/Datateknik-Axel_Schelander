import integer_input  #importerar heltalsmodueln

#skapar funktionen som söker efter perssonnumer i studentlistan
def search_student_by_id(student_list, id_number_to_find):
    for student in student_list:
        if student["id_number"] == id_number_to_find:
            return student
    return None

#Skapar listan school
school = []

#lägger till data från en anvöndartilläggd fill
def load_student_data():
    try:
        with open("students.txt", 'r') as file:
            lines = file.readlines()

            #procesar data från fillen i tre rads format, med data i den här strukturen, Pernum, efternamn, förnamn
            for i in range(0, len(lines), 3):
                id_number = lines[i].strip()
                last_name = lines[i + 1].strip()
                first_name = lines[i + 2].strip()

                #skapar uppsagsvärk med studentinformation
                student_info = {
                    "id_number": id_number,
                    "last_name": last_name,
                    "first_name": first_name
                }

                school.append(student_info)  #lägger till informationen till studentlistan

            print("Studentinformation har laddats från filen.")
    except FileNotFoundError:
        print("Ingen tidigare sparad studentinformation hittades.")

#laddar in studentdata från tidigare i programet
load_student_data()

while True:
    print("Välj ett alternativ:")
    print("1. Importera studentinformation från fil")
    print("2. Manuellt lägga till studenter")
    print("3. Avsluta")

    choice = input("Ange ditt val (1/2/3): ")

    if choice == '1':
        #ber anvödnare om filens filsökväg
        file_path = input("Ange sökväg till filen: ")

        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

                #tar data i stycken av tre rader
                for i in range(0, len(lines), 3):
                    id_number = lines[i].strip()
                    last_name = lines[i + 1].strip()
                    first_name = lines[i + 2].strip()

                    #skapar student info igen för filens information
                    student_info = {
                        "id_number": id_number,
                        "last_name": last_name,
                        "first_name": first_name
                    }

                    school.append(student_info)  # Add to the list as well

                    print("Studentinformation har importerats från filen.")

        except FileNotFoundError:
            print("Filen hittades inte.")
        except Exception as e:
            print(f"Ett fel inträffade: {str(e)}")

    elif choice == '2':
        # Manually add students and write them to the file
        num_students = integer_input.get_integer_input("Hur många elevers information vill du lägga till? ")

        with open("students.txt", 'a') as file:
            # Loop for input of student information
            for i in range(num_students):
                first_name = input("Studentens Förnamn {}:".format(i + 1))
                last_name = input("Studentens Efternamn {}:".format(i + 1))
                id_number = input("Studentens personnummer {}:".format(i + 1))

                # Create a dictionary for the student
                student_info = {
                    "id_number": id_number,
                    "last_name": last_name,
                    "first_name": first_name
                }

                school.append(student_info)  # Add to the list

                # Write the student data to the file
                file.write(id_number + "\n")
                file.write(last_name + "\n")
                file.write(first_name + "\n")

                print("Studentinformation har lagts till.")

    elif choice == '3':
        print("Programmet avslutas.")
        break

    else:
        print("Ogiltigt val. Ange 1, 2, eller 3.")

while True:
    # Ask the user if they want to search for students in the list
    list_input = input("Vill du söka efter elever i listan? Ja (j) Nej (n): ")

    if list_input.lower() == 'j':
        # Let the user search for students by their personal number
        search_id = input("Ange elevens personnummer du letar efter: ")
        found_student = search_student_by_id(school, search_id)

        if found_student:
            print("Elev hittad:")
            print("Namn: {} {}".format(found_student["first_name"], found_student["last_name"]))
            print("Personnummer: {}".format(found_student["id_number"]))
        else:
            print("Eleven med det angivna personnumret är inte en del av studentlistan.")
    elif list_input.lower() == 'n':
        # If the user doesn't want to search for students, print the entire list of students and exit the loop
        print("Studentlistan:")
        for student in school:
            print("Namn: {} {}, Personnummer: {}".format(student["first_name"], student["last_name"], student["id_number"]))
        break
    else:
        # If the user enters an incorrect input (not 'n' or 'j'), prompt them to enter 'n' or 'j' again
        print("Ogiltigt val, ange (j) eller (n) för att fortsätta.")
