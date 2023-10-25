school = []  # Initialize the school list

def search_student_by_id(id_number_to_find):
    for student in school:
        if student["id_number"] == id_number_to_find:
            return student
    return None



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










# Get the file path from the user
file_path = input("Enter the file path: ")

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Process the data in groups of three lines
        for i in range(0, len(lines), 3):
            id_number = lines[i].strip()
            last_name = lines[i + 1].strip()
            first_name = lines[i + 2].strip()

            # Create a dictionary for the student
            student_info = {
                "id_number": id_number,
                "last_name": last_name,
                "first_name": first_name
            }

            # Append the student information to the school list
            school.append(student_info)

    # Function to search for a student by id_number

    while True:
        listinput = input("Vill du söka efter elever i listan? ja (j) nej (n): ")
        if listinput.lower() == 'j':
            # Let the user search for students by their personal number
            search_id = input("Vad är eleven du letar efter personnummer: ")
            found_student = search_student_by_id(search_id)

            if found_student:
                print("")
                print("Student hittad:")
                print("Namn: {} {}".format(found_student["first_name"], found_student["last_name"]))
                print("Personnummer: {}".format(found_student["id_number"]))
            else:
                print("Studenten med det givna personnumret är inte en del av studentlistan.")
        elif listinput.lower() == 'n':
            # If the user doesn't want to search for students, print the entire list of students and exit the loop
            print("")
            print("Studentlistan:")
            for student in school:
                print("Name: {} {}, Personnummer: {}".format(student["first_name"], student["last_name"], student["id_number"]))
            break
        else:
            # If the user enters an incorrect input (not 'n' or 'j'), prompt them to enter 'n' or 'j' again
            print("Fel input, skriv (j) eller (n) för att fortsätta")

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")