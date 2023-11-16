import integer_input  # Import the module for integers

class Student:
    def __init__(self, id_number, first_name, last_name):
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, ID Number: {self.id_number}"

    def edit_info(self):
        print(f"Current information for the student:")
        print(str(self))
        self.first_name = input("Enter the new first name: ")
        self.last_name = input("Enter the new last name: ")
        self.id_number = input("Enter the new ID number: ")
        print("Student information has been edited.")

# Create a list for school
school = []

# Load student data from a file
def load_student_data():
    try:
        with open("student.txt", 'r') as file:
            lines = file.readlines()

            # Process data from the file in sets of three lines
            for i in range(0, len(lines), 3):
                id_number = lines[i].strip()
                last_name = lines[i + 1].strip()
                first_name = lines[i + 2].strip()

                # Create an instance of the Student class and add it to the school list
                student = Student(id_number, first_name, last_name)
                school.append(student)

            print("Student information has been loaded from the file.")
    except FileNotFoundError:
        print("No previously saved student information was found.")

# Edit the student function to use the new str representation and edit_info method
def edit_student(student_list, id_number_to_edit):
    for student in student_list:
        if student.id_number == id_number_to_edit:
            student.edit_info()
            return

    print("The student with the specified ID number is not part of the student list.")

# Create a function to delete student information
def delete_student(student_list, id_number_to_delete):
    for student in student_list:
        if student.id_number == id_number_to_delete:
            student_list.remove(student)
            print("Student information has been deleted.")
            return

    print("The student with the specified ID number is not part of the student list.")

# Create a function to search for a student by their ID number
def search_student_by_id(student_list, id_number_to_search):
    for student in student_list:
        if student.id_number == id_number_to_search:
            return student

    return None

load_student_data()  # Load student data from a previous session

while True:
    print("Choose an option:")
    print("1. Import student information from a file")
    print("2. Add students manually")
    print("3. Edit student information")
    print("4. Delete student information")
    print("5. Finish")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        # Ask the user for the file path
        file_path = input("Enter the file path: ")

        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

                # Process data in sets of three lines
                for i in range(0, len(lines), 3):
                    id_number = lines[i].strip()
                    last_name = lines[i + 1].strip()
                    first_name = lines[i + 2].strip()

                    # Create an instance of the Student class and add it to the school list
                    student = Student(id_number, first_name, last_name)
                    school.append(student)

                    print("Student information has been imported from the file.")

        except FileNotFoundError:
            print("The file was not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    elif choice == '2':
        # Add students manually and write them to the file
        num_students = integer_input.get_integer_input("How many students' information do you want to add? ")

        with open("students.txt", 'a') as file:
            # Loop for entering student information
            for i in range(num_students):
                first_name = input(f"Enter student {i + 1}'s first name: ")
                last_name = input(f"Enter student {i + 1}'s last name: ")
                id_number = input(f"Enter student {i + 1}'s ID number: ")

                # Create an instance of the Student class and add it to the school list
                student = Student(id_number, first_name, last_name)
                school.append(student)

                # Write student data to the file
                file.write(student.id_number + "\n")
                file.write(student.last_name + "\n")
                file.write(student.first_name + "\n")

                print("Student information has been added.")

    elif choice == '3':
        # Let the user enter the ID number to edit student information
        id_number_to_edit = input("Enter the ID number of the student you want to edit: ")
        edit_student(school, id_number_to_edit)

    elif choice == '4':
        # Let the user enter the ID number to delete student information
        id_number_to_delete = input("Enter the ID number of the student you want to delete: ")
        delete_student(school, id_number_to_delete)

    elif choice == '5':
        print("The program is ending.")
        break

    else:
        print("Invalid choice. Enter 1, 2, 3, 4, or 5.")

# Ask the user if they want to search for students in the list
list_input = input("Do you want to search for students in the list? Yes (y) No (n): ")

while list_input.lower() == 'y':
    # Let the user search for students with their ID number
    search_id = input("Enter the ID number of the student you are looking for: ")
    found_student = search_student_by_id(school, search_id)

    if found_student:
        print("Student found:")
        print(str(found_student))
    else:
        print("The student with the specified ID number is not part of the student list.")

    # Ask if the user wants to continue searching
    list_input = input("Do you want to search for more students? Yes (y) No (n): ")

if list_input.lower() == 'n':
    # If the user does not want to search for students, print the entire list of students and exit the loop
    print("Student list:")
    for student in school:
        print(str(student))
else:
    # If the user enters an incorrect choice (not 'n' or 'y'), prompt them to enter 'n' or 'y' again
    print("Invalid choice, program ending.")
