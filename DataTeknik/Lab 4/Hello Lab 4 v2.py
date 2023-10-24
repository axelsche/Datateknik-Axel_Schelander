import integer_input #importerrar heltalsmodelen från tidigare labbar

#startar listan med studentinformation
student_list = []

# Ask the user how many students they want to add
num_students = integer_input.get_integer_input("Hur många elevers information vill du skriva-in? ")

# Loop för input av studentinformation
for i in range(num_students):
    first_name = input("Studentens Förnamn {}:".format(i + 1))#felhantering av namn som limiterar input till strängar med text skulel reducera klodens användbarhet till namn som T.Ex X Æ A-12
    last_name = input("Studentens Efternamn {}:".format(i + 1))
    id_number = input("Studentents personnumer {}:".format(i + 1))
    print("")
    print ("Objekt skapats")
    print("")


    # Create a dictionary to store the student's information
    student_info = {
        "first_name": first_name,
        "last_name": last_name,
        "id_number": id_number
    }

    # lägertill studentinformationen till listan skapad tidigare
    student_list.append(student_info)

# Print the list of students
print("Listand med elevinformation:")
for student in student_list:
    print("Namn: {} ""{}, Personnummer: {}".format(student["first_name"], student["last_name"], student["id_number"]))